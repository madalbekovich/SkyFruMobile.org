from django.shortcuts import render
from rest_framework.generics import (
    GenericAPIView, CreateAPIView, ListAPIView)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from apps.helpers.common.service import ApiClient
from .services import Util
from .tasks import send_user_to_api
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


from .models import User
from .serializers import RegisterSerializer, LoginSerializer, VerifyEmailSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, ForgotPasswordVerifySerializer, UserInfoSerializer, SendMailSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        client_api = ApiClient(login="api_test_skyfru", password="api_test_skyfru")
        client_api.start_session()
        serializer = self.serializer_class(data=request.data)
        
        if not client_api.session_token:
            return Response(
                {
                    "response": False,
                    "message": "Внутренная ошибка.",
                    "code": "ERROR"
                }
            )
        
        if User.objects.filter(email=request.data["email"]).exists():
            return Response(
                {
                    "response": False,
                    "message": "Пользователь с таким электронным адресом уже существует.",
                    "code": "ERROR"
                }
            )

        if serializer.is_valid():
            email = serializer.data["email"]
            first_name = serializer.data["first_name"]
            last_name = serializer.data["last_name"]
            password = serializer.data["password"]
            phone = serializer.data["phone"]

            user = User(
                email=email, first_name=first_name, last_name=last_name, phone=phone
            )
            user.set_password(password)
            user.save()
            email_body = (
                "<div style='text-align: center;'>"
                f"<span style='font-size: 18px' >Уважаемый! {user.first_name}</span><br><br>"
                f"<span style='font-size: 18px'>Ваш код для подверждения аккаунта:</span><br><br>"
                f"<b style='font-size: 25px'>{user.code}</b>"
                "</div>"
            )

            email_data = {
                "email_body": email_body,
                "email_subject": "FLY-FLUR",
                "to_email": user.email,
            }

            Util.send_email(email_data)

            response = client_api.add_user(
                login=user.email,
                password=password,
                confirm_password=password,
                last_name=last_name,
                first_name=user.first_name,
                email=email,
                phone=phone,
            )

            if "user_id" in response:
                user.service_user_id = response['user_id']
                user.save()

            return Response(
                {
                    "response": True, 
                    "message": "Код подверждения отправлено на вашу почту!",
                    "code": "OK",
                    "description": response,
                }
            )
        return Response(serializer.errors)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = request.data.get("email")
            password = request.data.get("password")

            try:
                get_user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": "Пользователь с таким электронным адресом не существует",
                    }
                )

            user = authenticate(request, email=email, password=password)

            if not user:
                return Response(
                    {
                        "response": False,
                        "message": "Неверный пароль или логин!",
                    }
                )

            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "response": True,
                        "message": "Вход в систему выполнен успешно",
                        "token": token.key,
                    }
                )
            return Response(
                {
                    "response": False,
                    "message": "Подтвердите адрес электронной почты",
                    "is_active": False,
                }
            )

        return Response(serializer.errors)


# class LogoutView(GenericAPIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         auth_token = request.data.get('access')
#         if auth_token and auth_token.user == request.user:
#             auth_token.delete()
#         return Response({"message": "Вы успешно вышли из системы."}, status=status.HTTP_200_OK)


class VerifyEmailView(GenericAPIView):
    serializer_class = VerifyEmailSerializer
    
    def post(self, request):
        client_api = ApiClient(login="api_test_skyfru", password="api_test_skyfru")
        client_api.start_session()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data["code"]
            email = serializer.data["email"]

            try:
                user = User.objects.get(email=email)

                if user.is_active:
                    return Response({"message": "Аккаунт уже подтвержден"})

                if user.code == code:
                    user.is_active = True
                    user.save()

                    token, created = Token.objects.get_or_create(user=user)
                    return Response(
                        {
                            "response": True,
                            "message": "Пользователь успешно зарегистрирован.",
                            "token": token.key,
                        }
                    )
                
                return Response(
                    {"response": False, "message": "Введен неверный код"}
                )
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": "Пользователь с таким электронным адресом не существует",
                    }
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ChangePasswordView(GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            password = serializer.data["password"]
            confirm_password = serializer.data["confirm_password"]

            if password != confirm_password:
                return Response({"response": False, "message": "Пароли не совпадают"})

            user.set_password(password)
            user.save()

            return Response({"response": True, "message": "Пароль успешно обновлен"})
        return Response(serializer.errors)


class ForgotPassword(GenericAPIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data["email"]
            try:
                user = User.objects.get(email=email)
                user.save()

                email_body = (
                    "<div style='text-align: center;'>"
                    f"<span style='font-size: 18px' >Уважаемый! {user.first_name}</span><br><br>"
                    f"<span style='font-size: 18px'>Для сброса пароля подвердите код! Ваш код:</span><br><br>"
                    f"<b style='font-size: 25px'>{user.code}</b>"
                    "</div>"
                )

                email_data = {
                    "email_body": email_body,
                    "email_subject": "FLY-FLUR",
                    "to_email": user.email,
                }

                Util.send_email(email_data)

                return Response({"response": True, "message": "Код подверждения был отправлен на вашу электронную почту!"})
            except ObjectDoesNotExist:
                return Response({"response": False, "message": "Пользователь с таким электронным адресом не существует"})
        return Response(serializer.errors)


class ForgotPasswordVerifyView(GenericAPIView):
    serializer_class = ForgotPasswordVerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.data["code"]
            email = serializer.data["email"]
            try:
                user = User.objects.get(email=email)

                if user.code == code:
                    token, created = Token.objects.get_or_create(user=user)

                    return Response({"response": True, "token": token.key})
                return Response({"response": False, "message": "Введен неверный код"})
            except ObjectDoesNotExist:
                return Response({"response": False, "message": "Пользователь с таким электронным адресом не существует"})
        return Response(serializer.errors)


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user_info = UserInfoSerializer(request.user).data
        return Response(user_info)

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({"response": True, "message": "Ваш аккаунт удален!", "code": "OK"})

class UpdateUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer

    def patch(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": True, "message": "Данные успешно изменены.", "code": "OK"})
        return Response(serializer.errors)


class SendMailView(APIView):
    serializer_class = SendMailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not User.objects.filter(email=request.data["email"]).exists():
            return Response(
                {
                    "response": False,
                    "message": "Пользователь с таким электронным адресом не существует.",
                }
            )

        if serializer.is_valid():
            email = serializer.data["email"]
            user = User.objects.filter(email=email)
            user = User()
            print(f"Пользователь под именем {user.first_name}")

            email_body = (
                "<div style='text-align: center;'>"
                # f"<span style='font-size: 18px' >Уважаемый! {user.first_name}</span><br><br>"
                f"<span style='font-size: 18px'>Ваш код для подверждения аккаунта:</span><br><br>"
                f"<b style='font-size: 25px'>{user.code}</b>"
                "</div>"
            )

            email_data = {
                "email_body": email_body,
                "email_subject": "FLY-FLUR",
                "to_email": user.email,
            }

            Util.send_email(email_data)

            return Response({"response": True, "message": "Код подверждения отправлено на вашу почту!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
