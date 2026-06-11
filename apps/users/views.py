from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, VerifyEmailSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "User registered successfully. Please verify your email."
            },
            status=status.HTTP_201_CREATED,
        )
    
# Email verification view
class VerifyEmailAPIView(
    APIView
):
    def post(
        self,
        request,
    ):
        serializer = (
            VerifyEmailSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:
            serializer.save()

        except ValueError as e:
            return Response(
                {
                    "detail": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message":
                "Email verified successfully."
            },
            status=status.HTTP_200_OK,
        )