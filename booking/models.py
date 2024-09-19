from django.db import models

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Гость забронировавший стол")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Стол")
    start_datetime = models.DateTimeField(verbose_name="Дата и время бронирования")
    end_datetime = models.DateTimeField(verbose_name="Дата и время окончания бронирования", **NULLABLE)
    status = models.PositiveIntegerField(default=3, choices=status, verbose_name="Статус бронирования")

    def __str__(self):
        return f'{self.user} забронировал  {self.table} на  {self.start_datetime}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'


class RestaurantTeam(models.Model):
    employee_name = models.CharField(max_length=50, verbose_name="Имя сотрудника")
    position = models.CharField(max_length=50, verbose_name="Должность ")
    photo = models.ImageField(upload_to='booking/employee_photos/', verbose_name="Фото сотрудника")

    def __str__(self):
        return f'{self.employee_name} - {self.position}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
