from django.conf import settings
from django.core.mail import send_mail

from .utils import generate_verification_data

from django.contrib.auth import get_user_model

User = get_user_model()

def send_verification_email(*, user: User) -> None:
    """
    Send account verification email.
    """

    verification_data = generate_verification_data(user)

    verification_url = (
        f"http://localhost:5173/verify-email/"
        f"{verification_data['uid']}/"
        f"{verification_data['token']}"
    )

    subject = "Verify Your Email"

    message = (
        "Thank you for registering.\n\n"
        "Please verify your email by clicking "
        "the link below:\n\n"
        f"{verification_url}"
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )