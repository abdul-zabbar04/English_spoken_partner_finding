from django.urls import path

from .views import (
    RegisterAPIView,
    VerifyEmailAPIView,
    LoginAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("verify-email/", VerifyEmailAPIView.as_view(), name="verify-email"),
    path("login/", LoginAPIView.as_view(), name="login"),
]