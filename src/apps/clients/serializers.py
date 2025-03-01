from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов."},
    )

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
        ]

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        validate_password(password)

        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают!")

        return attrs

    def save(self, **kwargs):
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        phone = self.validated_data["phone"]

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        write_only=True,
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    token = serializers.CharField(read_only=True)


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.CharField(
        required=True,
    )
    code = serializers.IntegerField(
        required=True
    )

    class Meta:
        fields = ["email", "code"]


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True, 
        min_length=8, 
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
    confirm_password = serializers.CharField(
        required=True,
        min_length=8, 
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(
        required=True, 
        error_messages={"required": "Это поле обязательно."}
    )

    class Meta:
        fields = ["email"]


class ForgotPasswordVerifySerializer(serializers.Serializer):
    email = serializers.CharField()
    code = serializers.IntegerField(
        required=True, 
        error_messages={"required": "Это поле обязательно."}
    )

    class Meta:
        fields = ["email", "code"]