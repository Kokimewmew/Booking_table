# Generated by Django 5.1.1 on 2024-10-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_table_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_history',
            field=models.BooleanField(default=False, verbose_name='В истории'),
        ),
    ]
