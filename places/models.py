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


class TourImage(models.Model):
    ordinal_number = models.PositiveSmallIntegerField(
        "Порядковый номер", choices=[(1, "1"), (2, "2")]
    )
    image = models.ImageField("Изображение места")
    tour = models.ForeignKey(
        Tour,
        on_delete=models.PROTECT,
        verbose_name="Тур",
        related_name="images",
    )

    def __str__(self) -> str:
        return f"{self.ordinal_number} {self.tour.title}"

    class Meta:
        verbose_name = "Картинка тура"
        verbose_name_plural = "Картинки туров"
