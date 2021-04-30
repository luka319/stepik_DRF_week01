import requests
from django.core.management import BaseCommand
from users.models import User

# f=open(r'static/item_foodboxes.json',"wb") #открываем файл для записи, в режиме wb
# ufr = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json") #делаем запрос
# f.write(ufr.content) #записываем содержимое в файл; content запроса
# f.close()

# new_objects = []
# for people in peoples:
#     obj, created = People.objects.update_or_create(...)
#     if created:
#         new_objects.append(obj.id)

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json")
        response.raise_for_status()

        for users in response.json():
            try:
                User.objects.update_or_create(self, username=users['email'].split("@")[0])
            except ValueError:
                User.objects.update_or_create(self, username="John Dou_что-то не тоу")
            finally:
                obj, created = User.objects.update_or_create(self,
                    id=int(users['id']),
                    username=users['email'].split("@")[0],
                    first_name=users['info']['name'],
                    last_name=users['info']['surname'],
                    email=users['email'],
                    middle_name=users['info']['patronymic'],
                    phone=users["contacts"]["phoneNumber"],
                    address=users['city_kladr'],
                    ) # finally
                print(f"{obj=}, {created=}")

"""
AbstractUser:
   is_staff = models.BooleanField(
   is_active = models.BooleanField(
   date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # Помимо     стандартных    полей    AbstractUser:
    # middle_name(отчество) — CharField
    middle_name = models.CharField(max_length=255, verbose_name="отчество")
    # phone(телефон) — CharField.
    phone = models.CharField(max_length=60, verbose_name="телефон")
    # address (адрес) - CharField
    address = models.CharField(max_length=255,verbose_name="адрес")



"""
"""
    "id": 1,
    "email": "vanyavanya@ynadex.ru",
    "password": "DHRypOB99r",
    "info": {
      "surname": "Иванов",
      "name": "Иван",
      "patronymic": "Иванович"
    },
    "contacts" : {"phoneNumber": "8-999-777-66-00"},
    "city_kladr": "Санкт-Петербург",
    "premium" : false

"""