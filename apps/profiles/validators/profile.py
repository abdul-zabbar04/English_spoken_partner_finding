from zoneinfo import available_timezones

from django.core.exceptions import ValidationError


RESERVED_DISPLAY_NAMES = {
    "admin",
    "administrator",
    "support",
    "system",
    "root",
    "api",
    "staff",
    "null",
    "undefined",
}


def validate_display_name(value: str) -> str:
    """
    Validate display name.
    """

    value = value.strip()

    if len(value) < 3:
        raise ValidationError(
            "Display name must contain at least 3 characters."
        )

    if len(value) > 100:
        raise ValidationError(
            "Display name cannot exceed 100 characters."
        )

    if value.lower() in RESERVED_DISPLAY_NAMES:
        raise ValidationError(
            "This display name is not allowed."
        )

    return value


def validate_bio(value: str) -> str:
    """
    Validate profile bio.
    """

    value = value.strip()

    if len(value) > 500:
        raise ValidationError(
            "Bio cannot exceed 500 characters."
        )

    return value


def validate_country(value: str) -> str:
    """
    Validate ISO country code.
    """

    value = value.strip().upper()

    if value and len(value) != 2:
        raise ValidationError(
            "Country must be a valid ISO-3166 alpha-2 code."
        )

    return value


def validate_timezone(value: str) -> str:
    """
    Validate timezone.
    """

    if value not in available_timezones():
        raise ValidationError(
            "Invalid timezone."
        )

    return value