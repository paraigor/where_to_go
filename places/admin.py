from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    extra = 0
    readonly_fields = ["preview"]
    fields = ("image", "preview", "ordinal_number")

    def preview(self, obj):
        return format_html(
            mark_safe(f"<img src='{obj.image.url}' height='200' />")
        )


@admin.register(Place)
class TourDetailsAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "description_short", "description_long")}),
        ("Координаты", {"fields": ("longitude", "latitude")}),
    )
    search_fields = ["title"]
    inlines = [PlaceImageInline]


admin.site.register(PlaceImage)
