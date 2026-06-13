from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterAPIView,
    VerifyEmailAPIView,
    LoginAPIView,
    MeAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("verify-email/", VerifyEmailAPIView.as_view(), name="verify-email"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("me/", MeAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
]