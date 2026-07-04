from rest_framework import serializers

from apps.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    class Meta:
        model = Profile

        fields = (
            "email",
            "display_name",
            "profile_image",
            "bio",
            "country",
            "timezone",
            "english_level",
            "interests",
            "speaking_goals",
            "is_profile_completed",
        )

        read_only_fields = (
            "email",
            "is_profile_completed",
        )