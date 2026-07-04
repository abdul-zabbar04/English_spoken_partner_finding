from django.contrib import admin

from apps.profiles.models import SpeakingGoal


@admin.register(SpeakingGoal)
class SpeakingGoalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "created_at",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "slug",
        "created_at",
    )