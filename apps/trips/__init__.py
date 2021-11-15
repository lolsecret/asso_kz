from django.db.models import TextChoices


class UserRoles(TextChoices):
    DRIVER = "DRIVER", "Исполнитель"
    RIDER = "RIDER", "Заказчик"


class ServiceNames(TextChoices):
    WASTE_DISPOSAL_MACHINE = "WASTE_DISPOSAL_MACHINE", "Машина для утилизации отходов"
    ASPHALT_PAVER_MACHINE = "ASPHALT_PAVER_MACHINE", "Асфальтоукладчик"
    BULLDOZER = "BULLDOZER", "Бульдозер"

class TripStatus(TextChoices):
    REQUESTED = 'REQUESTED', 'Запрошен'
    STARTED = 'STARTED', 'Начата'
    IN_PROGRESS = 'IN_PROGRESS', "В процессе"
    COMPLETED = 'COMPLETED', "Завершена"