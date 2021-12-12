
import time

import pyotp
from django.utils import timezone
from django.utils.timezone import localtime
from django.conf import settings
from django.db import models, transaction
from phonenumbers import PhoneNumber
from apps.core.models import TimestampModel

# Create your models here.
from apps.sms.managers import OTPQueryset


class OTP(TimestampModel):
    code = models.CharField("OTP", max_length=12, db_index=True, editable=False)
    verified = models.BooleanField("Подтверждён", default=False, editable=False)
    # mobile_phone = PhoneNumberField("Мобильный телефон", editable=False)
    email = models.EmailField(
        "Email пользователя",
        null=True,
        blank=True
    )
    objects = OTPQueryset.as_manager()

    class Meta:
        verbose_name = "Одноразовый пароль"
        verbose_name_plural = "Одноразовые пароли"
        # unique_together = ("code", "mobile_phone")

    @classmethod
    def generate(cls, email):
        with transaction.atomic():
            instance = cls()
            instance.save()
            time_now_seconds = int(time.mktime(localtime(timezone.now()).timetuple())) + instance.pk
            code = "0000"
             # settings.SWAGGER_ENABLE:
             #    code = "0000"
            # else:
            #     hotp = pyotp.HOTP(settings.HOTP_KEY, digits=settings.OTP_LENGTH)
            #     code = hotp.at(time_now_seconds)
            instance.code = code
            instance.email = email
            instance.save()
        return code