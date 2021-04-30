import requests
from django.core.management import BaseCommand
from items.models import Item

# f=open(r'static/item_foodboxes.json',"wb") #открываем файл для записи, в режиме wb
# ufr = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json") #делаем запрос
# f.write(ufr.content) #записываем содержимое в файл;
# f.close()



class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json")
        response.raise_for_status()

        for item in response.json():
            try:
                # obj, created = Item.objects.update_or_create(title=item['title'],
                Item.objects.update_or_create(title=item['title'],
                                              description=item['description'],
                                              defaults={'title': 'вот так'} )
                # obj.save()
                # Item.objects.update_or_create(title=item['title'],
                #                               description=item['description'],
                #                               defaults={'title': 'вот так'} )
                # Item.objects.create(self, title=item['title'])
            except ValueError:
                Item.objects.update_or_create(title="что-то не то", defaults={'title': 'не так'})
                # Item.objects.create(self, title="что-то не то")
            finally:
                # obj, created = Item.objects.update_or_create(
                Item.objects.update_or_create(
                # Item.objects.create(
                    id=item['id'],
                    title=item['title'],
                    description=item['description'],
                    image=item['image'].split("/")[-1],
                    # https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json"
                    weight=item['weight_grams'],
                    price=item['price'],
                    defaults=None,
                )
                # obj.save()
            # print(f"{image=}")
            # input("===========")

    # def get_remote_image(self):
    #     if self.image_url and not self.image_file:
    #         img_temp = NamedTemporaryFile(delete=True)
    #         img_temp.write(urlopen(self.image_url).read())
    #         img_temp.flush()
    #         self.image_file.save(f"image_{self.pk}", File(img_temp))
    #     self.save()

# class Layout(models.Model):
#     image = models.ImageField('img', upload_to='path/')
#
# layout = Layout()
# layout.image = "path/image.png"
# layout.save()

