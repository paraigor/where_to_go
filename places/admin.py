from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    extra = 0
    readonly_fields = ["preview"]
    fields = ("image", "preview", "ordinal_number")

    def preview(self, obj):
        return format_html(
            "<img src='{}' height='200' style='max-width:400px; max-height:200px' />",
            obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "short_description", "long_description")}),
        ("Координаты", {"fields": ("longitude", "latitude")}),
    )
    search_fields = ["title"]
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    autocomplete_fields = ["place"]
