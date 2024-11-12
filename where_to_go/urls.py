from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places import views as index_views

urlpatterns = [
    path("", index_views.index),
    path("places/", include("places.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
