import json
from pathlib import Path

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Load location info to database"

    def add_arguments(self, parser):
        parser.add_argument("json_file")

    def handle(self, *args, **options):
        self.stdout.write("Loading location...")

        file_link = options["json_file"]
        if not (
            file_link.startswith("http://") or file_link.startswith("https://")
        ):
            file_link = Path(file_link)

            if file_link.exists():
                with open(file_link, encoding="utf8") as file:
                    location = json.load(file)
            else:
                raise CommandError("Wrong path to file")

        else:
            try:
                response = requests.get(file_link)
                response.raise_for_status()
            except (requests.HTTPError, requests.Timeout):
                raise CommandError("Wrong URL")
            location = response.json()

        place, created = Place.objects.get_or_create(
            title=location["title"],
            description_short=location["description_short"],
            description_long=location["description_long"],
            defaults={
                "longitude": location["coordinates"]["lng"],
                "latitude": location["coordinates"]["lat"],
            },
        )

        if created:
            for img_link in location["imgs"]:
                try:
                    response = requests.get(img_link)
                    response.raise_for_status()
                except (requests.HTTPError, requests.Timeout):
                    continue

                img_file_name = img_link.split("/")[-1]

                place_image = PlaceImage.objects.create(place=place)
                place_image.image.save(
                    img_file_name, ContentFile(response.content), save=True
                )

        self.stdout.write("Successfully loaded!")
