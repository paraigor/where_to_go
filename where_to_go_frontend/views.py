from django.db.models import Prefetch
from django.shortcuts import render

from places.models import Tour, TourImage


def index(request):
    tours = (
        Tour.objects.all()
        .prefetch_related("detailes")
        .prefetch_related(
            Prefetch(
                "detailes__images",
                queryset=TourImage.objects.order_by("ordinal_number"),
            )
        )
    )
    places = []
    for tour in tours:
        tour_detailes = tour.detailes
        place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [tour.longitude, tour.latitude],
            },
            "properties": {
                "title": tour.title,
                "placeId": tour.id,
                "details": {
                    "title": tour_detailes.title,
                    "imgs": [
                        img.image.url for img in tour_detailes.images.all()
                    ],
                    "description_short": tour_detailes.description_short,
                    "description_long": tour_detailes.description_long,
                    "coordinates": {
                        "lng": tour_detailes.longitude,
                        "lat": tour_detailes.latitude,
                    },
                }
                if tour_detailes
                else None,
            },
        }

        places.append(place)

    context = {
        "places_geojson": {
            "type": "FeatureCollection",
            "features": places,
        }
    }

    return render(request, "where_to_go_frontend/index.html", context)
