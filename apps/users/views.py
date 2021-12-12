
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import LogInSerializer, UserSerializer, OTPSerializer
from ..sms.services import send_email_otp, verify_otp


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        send_email_otp(email=email)

        return self.create(request, *args, **kwargs)


class ValidateOTPView(APIView):
    @swagger_auto_schema(request_body=OTPSerializer)
    def post(self, request, *args, **kwargs):
        otp = request.data.get("otp")
        email = request.data.get("email")
        verify_otp(otp, email=email)

        return Response(data={"success": True})


class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


