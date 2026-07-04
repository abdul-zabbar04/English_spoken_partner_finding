from __future__ import annotations

from pathlib import Path

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.translation import gettext_lazy as _
from PIL import Image, UnidentifiedImageError

from apps.profiles.constants import (
    PROFILE_IMAGE_ALLOWED_EXTENSIONS,
    PROFILE_IMAGE_ALLOWED_MIME_TYPES,
    PROFILE_IMAGE_MAX_HEIGHT,
    PROFILE_IMAGE_MAX_SIZE,
    PROFILE_IMAGE_MAX_WIDTH,
    PROFILE_IMAGE_MIN_HEIGHT,
    PROFILE_IMAGE_MIN_WIDTH,
)


def validate_extension(image: UploadedFile) -> None:
    """
    Validate the uploaded file extension.
    """
    extension = Path(image.name).suffix.lower()

    if extension not in PROFILE_IMAGE_ALLOWED_EXTENSIONS:
        raise ValidationError(
            _("Only JPG, JPEG, PNG and WEBP images are allowed.")
        )


def validate_content_type(image: UploadedFile) -> None:
    """
    Validate the uploaded file MIME type.
    """
    if image.content_type not in PROFILE_IMAGE_ALLOWED_MIME_TYPES:
        raise ValidationError(
            _("Unsupported image format.")
        )


def validate_file_size(image: UploadedFile) -> None:
    """
    Validate the uploaded file size.
    """
    if image.size > PROFILE_IMAGE_MAX_SIZE:
        raise ValidationError(
            _("Image size cannot exceed 1 MB.")
        )


def validate_image(image: UploadedFile) -> None:
    """
    Validate that the uploaded file is a valid image.
    """
    try:
        with Image.open(image) as img:
            img.verify()

    except (UnidentifiedImageError, OSError) as exc:
        raise ValidationError(
            _("Uploaded file is not a valid image.")
        ) from exc

    finally:
        image.seek(0)


def validate_dimensions(image: UploadedFile) -> None:
    """
    Validate image dimensions.
    """
    try:
        with Image.open(image) as img:
            width, height = img.size

            if (
                width < PROFILE_IMAGE_MIN_WIDTH
                or height < PROFILE_IMAGE_MIN_HEIGHT
            ):
                raise ValidationError(
                    _(
                        "Image dimensions are too small."
                    )
                )

            if (
                width > PROFILE_IMAGE_MAX_WIDTH
                or height > PROFILE_IMAGE_MAX_HEIGHT
            ):
                raise ValidationError(
                    _(
                        "Image dimensions exceed the maximum allowed."
                    )
                )

    finally:
        image.seek(0)


def validate_profile_image(image: UploadedFile) -> None:
    """
    Run all profile image validations.
    """
    validate_extension(image)
    validate_content_type(image)
    validate_file_size(image)
    validate_image(image)
    validate_dimensions(image)