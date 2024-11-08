from django.shortcuts import render


def index(request):
    return render(request, "where_to_go_frontend/index.html")
