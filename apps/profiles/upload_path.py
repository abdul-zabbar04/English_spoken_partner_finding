from __future__ import annotations

from django.utils import timezone
from pathlib import Path
from uuid import uuid4


def profile_image_upload_path(instance, filename: str) -> str:
    """
    Generate a unique upload path for a user's profile image.

    Example:
        profile_images/2026/07/550e8400e29b41d4a716446655440000.jpg
    """

    current_date = timezone.now()

    extension = Path(filename).suffix.lower()

    unique_filename = f"{uuid4().hex}{extension}"

    return (
        f"profile_images/"
        f"{current_date.year}/"
        f"{current_date.month:02d}/"
        f"{unique_filename}"
    )