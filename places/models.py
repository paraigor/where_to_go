from django.db import models


class Tour(models.Model):
    title = models.CharField("Название", max_length=200)
    description_short = models.CharField("Короткое описание", max_length=250)
    description_long = models.TextField("Полное описание")
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
