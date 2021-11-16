from django.db.models import TextChoices


class UserRoles(TextChoices):
    DRIVER = "DRIVER", "Исполнитель"
    RIDER = "RIDER", "Заказчик"


class ServiceNames(TextChoices):
    WASTE_DISPOSAL_MACHINE = "WASTE_DISPOSAL_MACHINE", "Машина для утилизации отходов"
    ASPHALT_PAVER_MACHINE = "ASPHALT_PAVER_MACHINE", "Асфальтоукладчик"
    BULLDOZER = "BULLDOZER", "Бульдозер"
    DRILLING_EQUIPMENT = "DRILLING_EQUIPMENT", "Буровое оборудование"
    TRACKED_ALL_TERRAIN_MACHINE = "TRACKED_ALL_TERRAIN_MACHINE", "Гусеничный вездеход"
    WHEELED_ALL_TERRAIN_MACHINE = "WHEELED_ALL_TERRAIN_MACHINE", "Колесный вездеход"
    GAS_TANKER = "GAS_TANKER", "Газозаправщик"
    GENERATOR = "GENERATOR", "Генератор"
    HYDRAULIC_DRILL = "HYDRAULIC_DRILL", "Гидробур"
    HYDRODYNAMIC_FLUSHING = "HYDRODYNAMIC_FLUSHING", "Гидродинамическая промывка"
    GRADER = "GRADER", "Грейдер"
    CRAWLER_CRANE = "CRAWLER_CRANE", "Гусеничный кран"
    CRUSHER_MACHINE = "CRUSHER_MACHINE", "Дробилка"
    RINK_MACHINE = "RINK_MACHINE", "Каток"
    MUNICIPAL_SPECIAL_MACHINE = "MUNICIPAL_SPECIAL_MACHINE", "Коммунальная спецтехника"
    COMPRESSOR = "COMPRESSOR", "Компрессор"
    MINI_EXCAVATOR = "MINI_EXCAVATOR", "Мини-экскаватор"
    MANIPULATOR = "MANIPULATOR", "Манипулятор"


class TripStatus(TextChoices):
    ACTIVE = 'ACTIVE', 'Активный'
    APPROVING = 'APPROVING', 'На подтверждении'
    APPROVED = 'APPROVED', "Подтвержден"
    ON_WAY = 'ON_WAY', 'В пути'
    WAITING = 'WAITING', 'В ожидании'
    ON_TASK = 'ON_TASK', 'На исполнении'
    FINISHED = 'FINISHED', 'Завершен'


class PaymentTypes(TextChoices):
    CASH = "CASH", "Наличные"
    CARD = "CARD", "Карта"