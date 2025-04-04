from django.shortcuts import render, get_object_or_404
from .models import Movie
def DetailMovie(request, movie_id):
    kino = get_object_or_404(Movie, id=movie_id)
    return render(request, 'detailmovie.html', {'kino': kino})

