from django.shortcuts import render
from kinolar.models import Movie
def DetailMovie(request):
    try:
        kino = Movie.objects.all()
    except Movie.DoesNotExist:
        kino = None
    return render(request, 'detailmovie.html', {'kino': kino})
