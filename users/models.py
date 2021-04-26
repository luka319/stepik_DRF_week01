from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# User (покупатель, наследуется от AbstractUser):
class User (AbstractUser):
    # Помимо     стандартных    полей    AbstractUser:
    # middle_name(отчество) — CharField
    middle_name = models.CharField(max_length=255, verbose_name="отчество")
    # phone(телефон) — CharField.
    phone = models.CharField(max_length=60, verbose_name="телефон")
    # address (адрес) - CharField
    address = models.CharField(max_length=255,verbose_name="адрес")

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

    def __str__(self):
        return f"пользователь - {self.id}"