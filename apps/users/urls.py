from django.urls import path

from .views import RegisterAPIView, VerifyEmailAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("verify-email/", VerifyEmailAPIView.as_view(), name="verify-email"),
]