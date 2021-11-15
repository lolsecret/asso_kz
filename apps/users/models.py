from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from apps.core.models import TimestampModel
from apps.trips import UserRoles, ServiceNames


class Services(TimestampModel):
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Список услуг"

    name = models.CharField(
        "Название техники/услуги",
        max_length=22,
        choices=ServiceNames.choices,
        default=ServiceNames.BULLDOZER
    )

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, mobile_phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not mobile_phone:
            raise ValueError('The given mobile_phone must be set')
        self.mobile_phone = mobile_phone
        user = self.model(mobile_phone=mobile_phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_phone, password=None, **extra_fields):
        """Create and save a regular User with the given mobile_phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_phone, password, **extra_fields)

    def create_superuser(self, mobile_phone, password, **extra_fields):
        """Create and save a SuperUser with the given mobile_phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile_phone, password, **extra_fields)


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_phone = models.CharField('phone number', validators=[phone_regex], max_length=17,
                             unique=True, null=True)  # validators should be a list
    role = models.CharField("Роль", max_length=20, choices=UserRoles.choices, default=UserRoles.RIDER)
    is_driver = models.BooleanField(default=False)
    is_rider = models.BooleanField(default=False)
    USERNAME_FIELD = 'mobile_phone'
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Rider(TimestampModel):
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="rider")

    def __str__(self):
        return f'"Клиент" {self.user}'


class Driver(TimestampModel):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнитель'
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="driver")
    service = models.ForeignKey(
        Services,
        verbose_name="Техника",
        on_delete=models.CASCADE,
        related_name='drivers',
        null=True, blank=True
    )

    def __str__(self):
        return f'"Заказчик" {self.user}'