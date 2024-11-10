from django.shortcuts import render

from places.models import Tour


def index(request):
    tours = (
        Tour.objects.all()
        .prefetch_related("details")
        .prefetch_related("details__images")
    )
    places = []
    for tour in tours:
        tour_details = tour.details
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
                    "title": tour_details.title,
                    "imgs": [
                        img.image.url for img in tour_details.images.all()
                    ],
                    "description_short": tour_details.description_short,
                    "description_long": tour_details.description_long,
                    "coordinates": {
                        "lng": tour_details.longitude,
                        "lat": tour_details.latitude,
                    },
                }
                if tour_details
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
