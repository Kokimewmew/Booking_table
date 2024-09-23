from django.contrib import admin

from booking.models import Services, Table, Reservation, RestaurantTeam


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'availability',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'start_datetime', 'end_datetime', 'status',)


@admin.register(RestaurantTeam)
class RestaurantTeamAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'position', 'photo',)
