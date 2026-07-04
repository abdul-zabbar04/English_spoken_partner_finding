from zoneinfo import available_timezones

from django.conf import settings
from django.db import models

from apps.profiles.upload_path import profile_image_upload_path
from apps.profiles.validators import (
    validate_profile_image,
    validate_display_name,
    validate_bio,
    validate_country,
    validate_timezone,
)


class EnglishLevel(models.TextChoices):
    A1 = "A1", "A1 - Beginner"
    A2 = "A2", "A2 - Elementary"
    B1 = "B1", "B1 - Intermediate"
    B2 = "B2", "B2 - Upper Intermediate"
    C1 = "C1", "C1 - Advanced"
    C2 = "C2", "C2 - Proficient"


TIMEZONE_CHOICES = sorted(
    [(tz, tz) for tz in available_timezones()],
    key=lambda timezone: timezone[0],
)


class Profile(models.Model):
    """
    Stores additional user information.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    display_name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            validate_display_name,
        ],
    )

    profile_image = models.ImageField(
        upload_to=profile_image_upload_path,
        validators=[validate_profile_image],
        blank=True,
    )

    bio = models.TextField(
        blank=True,
        validators=[
            validate_bio,
        ],
    )

    country = models.CharField(
        max_length=2,
        blank=True,
        db_index=True,
        validators=[
            validate_country,
        ],
    )

    timezone = models.CharField(
        max_length=64,
        choices=TIMEZONE_CHOICES,
        default="UTC",
        validators=[
            validate_timezone,
        ],
    )

    english_level = models.CharField(
        max_length=2,
        choices=EnglishLevel.choices,
        blank=True,
        db_index=True,
    )

    interests = models.ManyToManyField(
        "profiles.Interest",
        blank=True,
        related_name="profiles",
    )

    speaking_goals = models.ManyToManyField(
        "profiles.SpeakingGoal",
        blank=True,
        related_name="profiles",
    )

    is_profile_completed = models.BooleanField(
        default=False,
        db_index=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "profiles"

    def __str__(self):
        return self.display_name