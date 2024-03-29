from watchmate_app.models import Movie
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()

    data = {
        'movies': list(movies.values()),
    }

    return JsonResponse(data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)

    data = {
        "title": movie.title,
        "description": movie.description,
        "director":movie.director,
    }

    return JsonResponse(data)
