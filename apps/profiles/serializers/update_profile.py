from rest_framework import serializers

from apps.profiles.models import Profile


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

        fields = (
            "display_name",
            "profile_image",
            "bio",
            "country",
            "timezone",
            "english_level",
            "interests",
            "speaking_goals",
        )

    def validate_display_name(self, value):
        return value.strip()

    def validate_bio(self, value):
        return value.strip()