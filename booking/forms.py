from datetime import timedelta, time, datetime

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
        self.user = kwargs.pop('user', None)  # Получаем пользователя из контекста (если он есть)
        self.table = kwargs.pop('table')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data

        table = self.table
        start_date = cleaned_data.get('start_date')
        start_time = datetime.strptime(cleaned_data.get('start_time'), '%H:%M').time()

        # Рассчитываем время начала и конца бронирования с учетом 4-х часов до и после

        do_time = (datetime.combine(datetime.min, start_time) - timedelta(hours=4)).time()
        end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=4)).time()

        print(do_time, end_time)

        # Проверка на конфликт с существующими бронированиями
        existing_reservations = Reservation.objects.filter(
            table=table,
            start_date=start_date,
            start_time__gte=start_time,
            start_time__lt=end_time,
            start_time__range=(do_time, end_time),
            status__in=[1, 3],
        ).exclude(pk=self.instance.pk)  
        if existing_reservations.exists():
            raise ValidationError("Стол занят в это время.")

        # Проверка на существование активного бронирования у пользователя
        if self.user:  # Проверяем,  есть  ли  пользователь  в  контексте
            active_reservations = Reservation.objects.filter(
                user=self.user,
                status__in=[1, 3],  # "Подтвержден" and "Ожидание"
                end_datetime__isnull=True,
            ).exclude(pk=self.instance.pk)
            if active_reservations.exists():
                raise ValidationError("У вас уже есть активное бронирование.")

        return cleaned_data

    class Meta:
        model = Reservation
        fields = ('start_date', 'start_time',)
