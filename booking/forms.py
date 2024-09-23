from datetime import timedelta, time

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils import timezone

from booking.models import Services, Reservation
from users.forms import StyleFormMixin


class ServicesForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class ServicesModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Services
        fields = ("name", "description", "preview")


class ReservationForm(StyleFormMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        self.table = kwargs.pop('table')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data

        start_time = cleaned_data.get('start_datetime').time()
        end_time = cleaned_data.get('end_datetime').time() if cleaned_data.get('end_datetime') else None

        # Проверка, что бронирование происходит между 12:00 и 22:00
        if start_time < time(12, 0) or end_time > time(22, 0):
            raise ValidationError("Вы можете забронировать стол только с 12:00 до 22:00")

        if cleaned_data.get('start_datetime') is None:
            raise ValidationError("Необходимо указать дату и время начало бронирования")

        if cleaned_data.get('start_datetime') < timezone.now():
            raise ValidationError("Дата и время начала бронирования должны быть в будущем.")



        if cleaned_data.get('end_datetime') is None:

            existing_reservations = Reservation.objects.filter(
                table=self.table,
                start_datetime__lt=cleaned_data.get('start_datetime') + timedelta(hours=3),
                end_datetime__gt=cleaned_data.get('start_datetime'),
                status__in=[1, 3]

            )

        else:
            existing_reservations = Reservation.objects.filter(
                table=self.table,
                start_datetime__lt=cleaned_data.get('end_datetime'),
                end_datetime__gt=cleaned_data.get('start_datetime'),
                status__in=[1, 3]

            )

        if existing_reservations.exists():
            raise ValidationError("Стол занят в это время")

        return cleaned_data

    class Meta:
        model = Reservation
        fields = ('start_datetime', 'end_datetime',)
