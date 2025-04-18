from django.urls import path
from .views import (
    RegisterView, LoginView, VerifyEmailView,
    ChangePasswordView, ForgotPassword, ForgotPasswordVerifyView,
    UserInfoView, DeleteUserView, UpdateUserView, SendMailView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot-password'),
    path('forgot-password-verify/', ForgotPasswordVerifyView.as_view(), name='forgot-password-verify'),
    path('user-info/', UserInfoView.as_view()),
    path('logout/', DeleteUserView.as_view()),
    path('update-user-detail/', UpdateUserView.as_view()),
    # path('send-mail/', SendMailView.as_view()),
]