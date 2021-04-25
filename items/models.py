from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.fields.files import ImageFieldFile
# Create your models here.
from drf_week01.settings import MEDIA_IMAGE_DIR


class Item(models.Model): # (набор продуктов):
    # Создайте модель «Company – компания» с полями:
    title = models.CharField(max_length=255) #title (заголовок или наименование)
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
    price = models.DecimalField(default=0)

    def __str__(self):
        return f"{self.title} / {self.description}/ {self.image}"

# User (покупатель, наследуется от AbstractUser):
class User (AbstractUser):
    # Помимо     стандартных    полей    AbstractUser:
    # middle_name(отчество) — CharField
    middle_name = models.CharField(max_length=255)
    # phone(телефон) — CharField.
    phone = models.CharField(max_length=60)
    # address (адрес) - CharField
    address = models.CharField(max_length=255)

class Reviews(): # (отзывы)
    # author (связь с User) – ForeignKey
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="reviews")
    text = models.TextField() # (текст отзыва) – TextField
    created_at = models.DateTimeField() # (дата создания) - DateTimeField
    published_at = models.DateTimeField() # (дата публикации) – DateTimeField
    status = models.CharField(max_length=30) # (на модерации, опубликован, отклонен) – CharField

