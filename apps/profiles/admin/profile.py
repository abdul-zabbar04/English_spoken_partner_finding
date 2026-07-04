from django.contrib import admin

from apps.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "display_name",
        "user",
        "english_level",
        "country",
        "is_profile_completed",
        "created_at",
    )

    list_filter = (
        "english_level",
        "country",
        "is_profile_completed",
    )

    search_fields = (
        "display_name",
        "user__email",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25