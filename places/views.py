from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Place


def index(request):
    places = Place.objects.all().prefetch_related("images")
    locations = []
    for place in places:
        location = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "details": {
                    "title": place.title,
                    "imgs": [
                        img.image.url for img in place.images.all()
                    ],
                    "description_short": place.description_short,
                    "description_long": place.description_long,
                    "coordinates": {
                        "lng": place.longitude,
                        "lat": place.latitude,
                    },
                }
            },
        }

        locations.append(location)

    context = {
        "places_geojson": {
            "type": "FeatureCollection",
            "features": locations,
        }
    }

    return render(request, "places/index.html", context)


def place(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("images"),
        pk=place_id,
    )

    response = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        },
    }

    return JsonResponse(
        response,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 4},
    )
