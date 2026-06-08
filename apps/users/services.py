from django.contrib.auth import get_user_model

from .emails import send_verification_email

User = get_user_model()


def register_user(
    *,
    email: str,
    password: str,
) -> User:
    """
    Register a new user and send
    verification email.
    """

    user = User.objects.create_user(
        email=email,
        password=password,
    )

    send_verification_email(user)

    return user