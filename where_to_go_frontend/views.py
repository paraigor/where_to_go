from django.shortcuts import render

from places.models import Tour


def index(request):
    tours = Tour.objects.all().prefetch_related("images")
    places = []
    for tour in tours:
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
                    "title": tour.title,
                    "imgs": [img.image.url for img in tour.images.all()],
                    "description_short": tour.description_short,
                    "description_long": tour.description_long,
                    "coordinates": {
                        "lng": tour.longitude,
                        "lat": tour.latitude,
                    },
                },
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
