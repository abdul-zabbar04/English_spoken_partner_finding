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

# Verify user's email address
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import email_verification_token

def verify_user_email(
    *,
    uid: str,
    token: str,
) -> User:
    """
    Verify user's email.
    """

    try:
        user_id = force_str(
            urlsafe_base64_decode(uid)
        )

        user = User.objects.get(
            pk=user_id
        )

    except (
        User.DoesNotExist,
        ValueError,
        TypeError,
        OverflowError,
    ):
        raise ValueError(
            "Invalid verification link."
        )

    if not email_verification_token.check_token(
        user,
        token,
    ):
        raise ValueError(
            "Invalid or expired token."
        )

    if not user.is_verified:
        user.is_verified = True

        user.save(
            update_fields=["is_verified"]
        )

    return user