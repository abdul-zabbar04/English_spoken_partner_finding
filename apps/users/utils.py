from django.contrib.auth import get_user_model
from django.utils.encoding import (
    force_bytes,
    force_str,
)
from django.utils.http import (
    urlsafe_base64_encode,
)

from .tokens import (
    email_verification_token,
)

User = get_user_model()


def generate_verification_data(
    user: User,
) -> dict[str, str]:
    """
    Generate uid and token for email verification.
    """

    uid: str = force_str(
        urlsafe_base64_encode(
            force_bytes(user.pk)
        )
    )

    token: str = (
        email_verification_token.make_token(
            user
        )
    )

    return {
        "uid": uid,
        "token": token,
    }