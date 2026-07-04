from django.urls import path

from apps.profiles.views.profile import (
    MyProfileAPIView,
)

urlpatterns = [
    path(
        "me/",
        MyProfileAPIView.as_view(),
        name="my-profile",
    ),
]