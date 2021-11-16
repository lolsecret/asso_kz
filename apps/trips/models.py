import uuid

from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.shortcuts import reverse
from apps.core.models import TimestampModel
from apps.trips import TripStatus, PaymentTypes
from django.conf import settings

from apps.users.models import Driver, Rider


class Trip(TimestampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.JSONField(
        verbose_name="Адрес",
        default=list,
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=TripStatus.choices,
        default=TripStatus.ACTIVE,
        db_index=True,
    )
    driver = models.ForeignKey(
        Driver,
        verbose_name="Исполнитель",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_driver'
    )
    rider = models.ForeignKey(
        Rider,
        verbose_name="Заказчик",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_rider'
    )
    payment_type = models.CharField(
        verbose_name="Тип оплаты",
        max_length=20,
        choices=PaymentTypes.choices,
        default=PaymentTypes.CASH,
        db_index=True,
    )
    price = models.CharField(
        verbose_name="Цена",
        max_length=7,
        null=True,
        blank=True,
    )
    comment = models.CharField(
        verbose_name="Комментарий",
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('trip:trip_detail', kwargs={'trip_id': self.id})

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
