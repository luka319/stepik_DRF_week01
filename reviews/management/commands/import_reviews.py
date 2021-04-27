import requests
from django.core.management import BaseCommand
from reviews.models import Reviews

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get("https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json")
        response.raise_for_status()

        for review in response.json():
            try:
                Reviews.objects.update_or_create(self,published_at=review['published_at'])
            except ValueError:
                Reviews.objects.update_or_create(self, published_at="1913-01-02")
            finally:
                Reviews.objects.update_or_create(self,
                    id=int(review['id']),
                    author=review['author'],
                    text=review['content'],
                    created_at=review['created_at'],
                    published_at=review['published_at'],
                    status=review['status'],
            )