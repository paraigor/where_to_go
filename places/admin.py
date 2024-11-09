from django.contrib import admin

from .models import Tour, TourDetailes, TourImage


@admin.register(TourDetailes)
class TourDetailesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "description_short", "description_long")}),
        ("Координаты", {"fields": ("longitude", "latitude")}),
    )

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "detailes")}),
        ("Координаты", {"fields": ("longitude", "latitude")}),
    )

admin.site.register(TourImage)
