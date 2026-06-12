from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .services import register_user, authenticate_user


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        return value.lower().strip()
    
    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = register_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
    

# email verification serializer
class VerifyEmailSerializer(
    serializers.Serializer
):
    uid = serializers.CharField()
    token = serializers.CharField()

    def save(self):
        from .services import (
            verify_user_email
        )

        return verify_user_email(
            uid=self.validated_data["uid"],
            token=self.validated_data["token"],
        )
    
# login serializer

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        return value.strip().lower()

    def validate(self, attrs):
        attrs["user"] = authenticate_user(
            email=attrs["email"],
            password=attrs["password"],
        )
        return attrs