from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.fields.files import ImageFieldFile
# Create your models here.
from drf_week01.settings import MEDIA_IMAGE_DIR


class Item(models.Model): # (набор продуктов):
    # Создайте модель «Company – компания» с полями:
    title = models.CharField(max_length=255, verbose_name="заголовок") #title (заголовок или наименование)
    description= models.TextField()  # description (описание) — TextField;
    image = models.ImageField(default="",  #image (картинка) – ImageField;
                             upload_to=MEDIA_IMAGE_DIR,
                             height_field='height_field',
                             width_field='width_field')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    # weight (вес в граммах) – PositiveSmallIntegerField;
    weight = models.PositiveSmallIntegerField(default=0)
    # price (цена в рублях) – DecimalField;
    price = models.DecimalField(max_digits=9, decimal_places=8)

    class Meta:
        verbose_name='Набор'
        verbose_name_plural='Наборы'

    def __str__(self):
        # return f"{self.title} / {self.description}/ {self.image}"
        return f"{self.title}"





