from rest_framework import serializers

from .services import register_user


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        return value.lower().strip()

    def create(self, validated_data):
        user = register_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user