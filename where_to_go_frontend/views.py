from django.shortcuts import render

from places.models import Place


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

    return render(request, "where_to_go_frontend/index.html", context)
