from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField("Название", max_length=200)
    short_description = models.CharField("Короткое описание", max_length=250)
    long_description = tinymce_models.HTMLField("Полное описание")
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(
                fields=["longitude", "latitude"], name="unigue_coordinates"
            ),
        ]
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class PlaceImage(models.Model):
    ordinal_number = models.PositiveSmallIntegerField(
        "Порядковый номер", default=0
    )
    image = models.ImageField("Фото локации", null=True)
    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        verbose_name="Локация",
        related_name="images",
    )

    def __str__(self) -> str:
        return f"{self.ordinal_number} {self.place.title}"

    class Meta:
        ordering = ["ordinal_number"]
        verbose_name = "Фото локации"
        verbose_name_plural = "Фото локаций"
