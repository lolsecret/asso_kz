from uuid import uuid4

from django.db import models
from django.utils.timezone import localtime


class TimestampModel(models.Model):
    created_at = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
    )
    updated_at = models.DateTimeField(
        "Время последнего изменения", auto_now=True, db_index=True
    )

    class Meta:
        abstract = True

    @property
    def created_at_pretty(self):
        return localtime(self.created_at).strftime("%d.%m.%Y %H:%M:%S")
    created_at_pretty.fget.short_description = "Время создания"

    @property
    def updated_at_pretty(self):
        return localtime(self.updated_at).strftime("%d.%m.%Y %H:%M:%S")
    updated_at_pretty.fget.short_description = "Время последнего изменения"


class UUIDModel(models.Model):
    uuid = models.UUIDField("Идентификатор", default=uuid4, unique=True, editable=False)

    class Meta:
        abstract = True