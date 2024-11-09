from django.contrib import admin

from .models import Tour, TourDetailes, TourImage


class TourImageInline(admin.TabularInline):
    model = TourImage
    fields = ("image", "ordinal_number")
    extra = 0


@admin.register(TourDetailes)
class TourDetailesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "description_short", "description_long")}),
        ("Координаты", {"fields": ("longitude", "latitude")}),
    )
    inlines = [TourImageInline]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "detailes")}),
        ("Координаты", {"fields": ("longitude", "latitude")}),
    )

admin.site.register(TourImage)
