from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    RegisterSerializer,
    VerifyEmailSerializer,
    LoginSerializer,
)


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
    
# Login view
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView):
    def post(self, request):
        serializer= LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)

        user= serializer.validated_data["user"]
        refresh= RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "email": user.email,
                }
            },
            status=status.HTTP_200_OK,
        )

# Me view to get current user details
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "email": user.email,
            "is_verified": user.is_verified,
        })