
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import LogInSerializer, UserSerializer


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_otp(mobile_phone=self.credit.borrower_data.mobile_phone, lead_id=self.credit.lead_id)

class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


