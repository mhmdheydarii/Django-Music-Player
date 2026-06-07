from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
import random
from django.core.files import File
from pathlib import Path
from music.models import Category

BASE_DIR = Path(__file__).resolve().parent

class Command(BaseCommand):
    help = "Generate fake categories"

    def handle(self, *args, **kwargs):
        fake = Faker()

        image_list = [
            "category_images/image1.jpg",
            "category_images/image2.jpg",
            "category_images/image3.jpg",
            "category_images/image4.jpg",
            "category_images/image5.jpg",                 
        ]

        random.shuffle(image_list)

        for selected_image in image_list:
            name = fake.word().title()

            with open(BASE_DIR / selected_image, "rb") as img:
                Category.objects.create(
                    name=name,
                    slug=slugify(name, allow_unicode=True),
                    image=File(img, name=Path(selected_image).name)
                )
        
        self.stdout.write(self.style.SUCCESS("Successfully generated 5 fake categories"))
