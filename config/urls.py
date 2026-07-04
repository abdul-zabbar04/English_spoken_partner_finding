from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/users/", include("apps.users.urls")),
    path("profile/", include("apps.profiles.urls")),
]
