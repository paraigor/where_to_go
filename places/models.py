from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)
    short_description = models.TextField("Короткое описание", blank=True)
    long_description = tinymce_models.HTMLField("Полное описание", blank=True)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    class Meta:
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(
                fields=["longitude", "latitude"], name="unigue_coordinates"
            ),
        ]
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self) -> str:
        return self.title


class PlaceImage(models.Model):
    ordinal_number = models.PositiveSmallIntegerField(
        "Порядковый номер", default=0
    )
    image = models.ImageField("Фото локации")
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Локация",
        related_name="images",
    )

    class Meta:
        indexes = [models.Index(fields=["ordinal_number"])]
        ordering = ["ordinal_number"]
        verbose_name = "Фото локации"
        verbose_name_plural = "Фото локаций"

    def __str__(self) -> str:
        return f"Photo {self.ordinal_number} {self.place.title if self.place else None}"
