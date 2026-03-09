from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):

    movies = Movie.objects.all()
    output = ", ".join([item.title for item in movies])

    return HttpResponse(output)


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return HttpResponse(movie)
