from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from users.models import User

class Reviews(): # (отзывы)
    STATUS_CHOICES = (
        ('new', 'на модерации'),
        ('published', 'опубликовано'),
        ('hidden', 'скрыто'),
    )
    # author (связь с User) – ForeignKey
    author = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE,
                                related_name="reviews",
                                verbose_name="автор")
    text = models.TextField() # (текст отзыва) – TextField
    created_at = models.DateTimeField(auto_now=True) # (дата создания) - DateTimeField
    published_at = models.DateTimeField() # (дата публикации) – DateTimeField
    status = models.CharField(choices=STATUS_CHOICES,
                              default="new",
                              max_length=30)
    # (на модерации, опубликован, отклонен) – CharField
    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

    def __str__(self):
        # return f"Отзыв номер - {self.pk}"
        return f"Отзыв номер - {self.id}"
