from datetime import datetime
from django.db import models
from django.utils import timezone

from booking.validators import validate_start_date
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Services(models.Model):
    name = models.CharField(max_length=100, verbose_name="Услуга")
    description = models.TextField(verbose_name="Описание услуги", **NULLABLE)
    preview = models.ImageField(upload_to='booking/services_photos/', verbose_name="Фото услуги")

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Table(models.Model):
    number = models.IntegerField(verbose_name="Номер стола")
    seats = models.IntegerField(verbose_name="Количество мест")
    availability = models.BooleanField(verbose_name="Доступность")

    image = models.ImageField(upload_to='booking/table_images/', blank=True, verbose_name='Изображение  стола')

    def __str__(self):
        return f' {self.number} столик на {self.seats} гостей'

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'


class Reservation(models.Model):
    status = [
        (1, 'Подтвержден'),
        (2, 'Отменен'),
        (3, 'Ожидание')
    ]

    choice_time = [
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
        ('22:00', '22:00'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Гость забронировавший стол")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Стол")
    start_date = models.DateField(verbose_name="Дата бронирования", default=datetime.now,
                                  validators=[validate_start_date]
                                  )
    start_time = models.CharField(verbose_name="Время бронирования",
                                  default='12:00',
                                  choices=choice_time)
    end_datetime = models.DateTimeField(blank=True, null=True, verbose_name="Время окончания бронирования")

    status = models.PositiveIntegerField(default=3, choices=status, verbose_name="Статус бронирования")

    is_history = models.BooleanField(default=False, verbose_name="В истории")

    def __str__(self):
        return f'{self.user} забронировал  {self.table} на  {self.start_date}'


    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        unique_together = ('table', 'start_date', 'start_time')


class RestaurantTeam(models.Model):
    employee_name = models.CharField(max_length=50, verbose_name="Имя сотрудника")
    position = models.CharField(max_length=50, verbose_name="Должность ")
    photo = models.ImageField(upload_to='booking/employee_photos/', verbose_name="Фото сотрудника")

    def __str__(self):
        return f'{self.employee_name} - {self.position}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return f'{self.name} - {self.created_at}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
