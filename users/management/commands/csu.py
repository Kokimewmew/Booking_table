from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")  # Заполните вашу почту как администратора
        user.set_password("123qwe")  # Задайте пароль
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
