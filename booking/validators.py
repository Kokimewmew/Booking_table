from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_start_date(value):
    if value < timezone.now().date():
        raise ValidationError('Дата бронирования не может быть раньше сегодняшней.')
    # pass
