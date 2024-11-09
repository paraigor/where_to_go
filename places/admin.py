from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Tour, TourDetailes, TourImage


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 0
    readonly_fields = ["preview"]
    fields = ("image", "preview", "ordinal_number")

    def preview(self, obj):
        return format_html(
            mark_safe(f"<img src='{obj.image.url}' height='200' />")
        )


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
