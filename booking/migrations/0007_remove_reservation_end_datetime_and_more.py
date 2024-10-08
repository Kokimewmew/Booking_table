# Generated by Django 5.1.1 on 2024-09-28 14:22

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_reservation_start_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now, validators=[django.core.validators.MinValueValidator(datetime.datetime.now), django.core.validators.MaxValueValidator(datetime.datetime(2024, 10, 12, 19, 22, 17, 821717))], verbose_name='Дата бронирования'),
        ),
    ]
