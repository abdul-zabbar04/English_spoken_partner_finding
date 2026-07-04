from django.contrib.auth import get_user_model

from apps.profiles.models import Profile

User = get_user_model()


def get_profile(*, user: User) -> Profile:
    """
    Return profile with all required relations.
    """

    return (
        Profile.objects
        .select_related("user")
        .prefetch_related(
            "interests",
            "speaking_goals",
        )
        .get(user=user)
    )