import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get("https://jsonkeeper.com/...")
        response.raise_for_status()

        for book in response.json():
            Book.objects.create(

            )