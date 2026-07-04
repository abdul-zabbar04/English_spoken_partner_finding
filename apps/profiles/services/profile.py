from django.db import transaction

from apps.profiles.models import Profile


def update_profile_completion_status(profile: Profile) -> None:
    """
    Update profile completion status.
    """

    completed = all(
        [
            profile.display_name,
            profile.bio,
            profile.country,
            profile.english_level,
            profile.interests.exists(),
            profile.speaking_goals.exists(),
        ]
    )

    if profile.is_profile_completed != completed:
        profile.is_profile_completed = completed

        profile.save(
            update_fields=[
                "is_profile_completed",
            ]
        )


@transaction.atomic
def update_profile(
    *,
    profile: Profile,
    validated_data: dict,
) -> Profile:

    interests = validated_data.pop(
        "interests",
        None,
    )

    speaking_goals = validated_data.pop(
        "speaking_goals",
        None,
    )

    for field, value in validated_data.items():
        setattr(profile, field, value)

    profile.save()

    if interests is not None:
        profile.interests.set(interests)

    if speaking_goals is not None:
        profile.speaking_goals.set(
            speaking_goals
        )

    update_profile_completion_status(profile)

    return profile