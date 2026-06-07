from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.files import File
import random
from music.models import Singer, Music, Category
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Command(BaseCommand):
    help = "Generate fake categories"

    def handle(self, *args, **kwargs):
        fake = Faker()

        image_list = [
            "singer_images/image2.jpg",
            "singer_images/image3.jpg",
            "singer_images/image4.jpg",
            "singer_images/image5.jpg",
            "singer_images/image6.jpg",
            "singer_images/image7.jpg",
            "singer_images/image8.jpg",
            "singer_images/image9.jpg",
            "singer_images/image10.jpg",
        ]

        categories = Category.objects.all()
        random.shuffle(image_list)

        for selected_image in image_list:
            name =  fake.name_male()
            selected_categories = random.choice(categories)
            slug = slugify(name, allow_unicode=True)
            year_started=fake.random_int(min=1950, max=2026)
            popularity = fake.boolean(chance_of_getting_true=80)


            with open(BASE_DIR / selected_image, "rb") as img:
                singer = Singer.objects.create(
                    name=name,
                    slug=slug,
                    image=File(img, name=Path(selected_image).name),
                    year_started=year_started,
                    popularity=popularity
                )
            singer.category = selected_categories
            singer.save()
        
        self.stdout.write(self.style.SUCCESS("Successfully generated 10 fake products"))