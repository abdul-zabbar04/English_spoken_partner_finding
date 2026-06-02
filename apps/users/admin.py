from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # it's overriding the default add_fieldsets to remove the username field
    add_fieldsets = None
    filter_horizontal = ()

    list_display = ("email", "is_verified", "is_staff", "is_active")
    list_filter = ("is_verified", "is_staff", "is_active")

    ordering = ("email",)
    search_fields = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_verified",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )