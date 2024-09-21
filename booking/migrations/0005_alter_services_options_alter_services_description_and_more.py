# Generated by Django 5.1.1 on 2024-09-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_services_remove_reservationhistory_reservation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание услуги'),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Услуга'),
        ),
    ]
