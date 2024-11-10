from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Tour


def place(request, place_id):
    tour = get_object_or_404(
        Tour.objects.prefetch_related("details").prefetch_related(
            "details__images"
        ),
        pk=place_id,
    )
    tour_details = tour.details

    response = {
        "title": tour_details.title,
        "imgs": [img.image.url for img in tour_details.images.all()],
        "description_short": tour_details.description_short,
        "description_long": tour_details.description_long,
        "coordinates": {
            "lng": tour_details.longitude,
            "lat": tour_details.latitude,
        },
    }

    return JsonResponse(
        response,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 4},
    )
