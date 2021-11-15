import uuid

from django.db import models
from django.shortcuts import reverse
from apps.core.models import TimestampModel
from apps.trips import TripStatus, ServiceNames
from django.conf import settings

from apps.users.models import Driver, Rider





class Trip(TimestampModel):  # new
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pick_up_address = models.CharField(max_length=255, verbose_name="Точка А")
    drop_off_address = models.CharField(max_length=255, verbose_name="Точка Б")
    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=TripStatus.choices,
        default=TripStatus.REQUESTED,
        db_index=True,
    )
    driver = models.ForeignKey(
        Driver,
        verbose_name="Заказчик",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_driver'
    )
    rider = models.ForeignKey(
        Rider,
        verbose_name="Исполнитель",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_rider'
    )

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('trip:trip_detail', kwargs={'trip_id': self.id})

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
