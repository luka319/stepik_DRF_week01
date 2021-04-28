import requests
from django.core.management import BaseCommand
from items.models import Item

f=open(r'static/item_foodboxes.json',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл;
f.close()



class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json")
        response.raise_for_status()

        for item in response.json():
            try:
                Item.objects.update_or_create(self, title=item['title'],
                                              description=item['description'],
                                              defaults={'title': 'вот так'} )
                # Item.objects.update_or_create(title=item['title'],
                #                               description=item['description'],
                #                               defaults={'title': 'вот так'} )
                # Item.objects.create(self, title=item['title'])
            except ValueError:
                Item.objects.update_or_create(self, title="что-то не то", defaults={'title': 'не так'})
                # Item.objects.create(self, title="что-то не то")
            finally:
                Item.objects.update_or_create(self,
                # Item.objects.create(
                    id=item['id'],
                    title=item['title'],
                    description=item['description'],
                    image=item['image'],
                    weight=item['weight_grams'],
                    price=item['price'],
                    defaults=None,
                )

