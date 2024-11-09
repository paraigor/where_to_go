from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Tour


def place(request, place_id):
    tour = get_object_or_404(
        Tour.objects.prefetch_related("detailes").prefetch_related(
            "detailes__images"
        ),
        pk=place_id,
    )
    tour_detailes = tour.detailes

    response = {
        "title": tour_detailes.title,
        "imgs": [img.image.url for img in tour_detailes.images.all()],
        "description_short": tour_detailes.description_short,
        "description_long": tour_detailes.description_long,
        "coordinates": {
            "lng": tour_detailes.longitude,
            "lat": tour_detailes.latitude,
        },
    }

    return JsonResponse(
        response,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 4},
    )
