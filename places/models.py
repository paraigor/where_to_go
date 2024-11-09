from django.db import models


class TourDetailes(models.Model):
    title = models.CharField("Название", max_length=200)
    description_short = models.CharField("Короткое описание", max_length=250)
    description_long = models.TextField("Полное описание")
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Детали тура"
        verbose_name_plural = "Детали туров"


class Tour(models.Model):
    title = models.CharField("Название", max_length=200)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")
    detailes = models.ForeignKey(
        TourDetailes,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Детали тура",
        related_name="tour",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class TourImage(models.Model):
    ordinal_number = models.PositiveSmallIntegerField(
        "Порядковый номер", default=2
    )
    image = models.ImageField("Изображение места")
    tour_detailes = models.ForeignKey(
        TourDetailes,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Тур",
        related_name="images",
    )

    def __str__(self) -> str:
        return f"{self.ordinal_number} {self.tour_detailes.title}"

    class Meta:
        ordering = ["ordinal_number"]
        verbose_name = "Картинка тура"
        verbose_name_plural = "Картинки туров"
