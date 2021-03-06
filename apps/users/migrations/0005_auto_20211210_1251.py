# Generated by Django 3.2.9 on 2021-12-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(choices=[('WASTE_DISPOSAL_MACHINE', 'Машина для утилизации отходов'), ('ASPHALT_PAVER_MACHINE', 'Асфальтоукладчик'), ('BULLDOZER', 'Бульдозер'), ('DRILLING_EQUIPMENT', 'Буровое оборудование'), ('TRACKED_ALL_TERRAIN_MACHINE', 'Гусеничный вездеход'), ('WHEELED_ALL_TERRAIN_MACHINE', 'Колесный вездеход'), ('GAS_TANKER', 'Газозаправщик'), ('GENERATOR', 'Генератор'), ('HYDRAULIC_DRILL', 'Гидробур'), ('HYDRODYNAMIC_FLUSHING', 'Гидродинамическая промывка'), ('GRADER', 'Грейдер'), ('CRAWLER_CRANE', 'Гусеничный кран'), ('CRUSHER_MACHINE', 'Дробилка'), ('RINK_MACHINE', 'Каток'), ('MUNICIPAL_SPECIAL_MACHINE', 'Коммунальная спецтехника'), ('COMPRESSOR', 'Компрессор'), ('MINI_EXCAVATOR', 'Мини-экскаватор'), ('MANIPULATOR', 'Манипулятор')], default='BULLDOZER', max_length=50, verbose_name='Название техники/услуги'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email покупателя'),
        ),
    ]
