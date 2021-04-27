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

"""
    "id": 1,
    "title": "Семейная промо-коробка",
    "description": "Набор продуктов на каждый день. Если надоело думать над составом заказа, или вы у нас первый раз — это отличный выбор. Из этих продуктов можно приготовить больше 10 блюд на завтрак, обед или ужин. Сорта продуктов могут меняться, в зависимости от наличия товаров. \n\nСостав: яблоки, бананы, огурцы, помидоры, зелень, картофель, морковь, репчатый лук, паста, рис, творог, молоко, сметана, сыр, сардельки, яйца, запечённое филе куриной грудки, пельмени, печенье.",
    "image": "https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/static/foodb1.jpg",
    "weight_grams": 9200,
//    "size": [310,260,380],
    "price": "3000.00",
//    "cat": 2

"""



