# Generated by Django 5.1.1 on 2024-09-28 14:32

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_reservation_end_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now, validators=[django.core.validators.MinValueValidator(datetime.datetime.now), django.core.validators.MaxValueValidator(datetime.datetime(2024, 10, 12, 19, 32, 1, 829169))], verbose_name='Дата бронирования'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_time',
            field=models.CharField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00')], default='12:00', max_length=5, verbose_name='Время бронирования'),
        ),
    ]
