from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from apps.profiles.selectors import get_profile
from apps.profiles.serializers.profile import (
    ProfileSerializer,
)
from apps.profiles.serializers.update_profile import (
    ProfileUpdateSerializer,
)
from apps.profiles.services.profile import (
    update_profile,
)


class MyProfileAPIView(GenericAPIView):

    permission_classes = (
        IsAuthenticated,
    )

    def get(self, request):
        profile = get_profile(
            user=request.user,
        )

        serializer = ProfileSerializer(
            profile,
        )

        return Response(
            serializer.data,
        )

    def patch(self, request):

        profile = get_profile(
            user=request.user,
        )

        serializer = ProfileUpdateSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        profile = update_profile(
            profile=profile,
            validated_data=serializer.validated_data,
        )

        return Response(
            ProfileSerializer(profile).data,
            status=status.HTTP_200_OK,
        )