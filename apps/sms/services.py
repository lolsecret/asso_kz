import logging
from datetime import timedelta
from typing import Tuple, Union

from django.db import transaction
from django.urls import reverse
from django.utils import timezone
from phonenumbers import PhoneNumber
from django.conf import settings
from django.core.mail import send_mail

from apps.sms.exceptions import InvalidOTP
from apps.sms.models import OTP


def send_email(subject, msg, recipient):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, msg, email_from, [recipient])


def send_email_otp(email):
    otp = OTP.generate(email)
    msg = f"Ваш OTP код для регистрации в приложении asso_kz: {otp}"
    subject = "OTP Code"
    send_email(
        recipient=email, subject=subject, msg=msg
    )


# def send_otp(mobile_phone: PhoneNumber, lead_id=None):
#     otp = OTP.generate(mobile_phone)
#     send_sms(
#         recipient=str(mobile_phone), template_name=SMSType.OTP, lead_id=lead_id, kwargs={"otp": otp}
#     )


def verify_otp(code: str, email, save=False, raise_exception=True):
    otp = OTP.objects.active().filter(email=email).last()
    if not otp or otp.code != code:
        if raise_exception:
            raise InvalidOTP
        else:
            return False

    if save:
        otp.verified = True
        otp.save(update_fields=["verified"])

    return True