from django.shortcuts import render
from django.contrib import messages
from kinolar.models import Movie, CategoryYili
def home(request):
    kino = Movie.objects.all()
    multfilmlar = Movie.objects.filter(categorykinolar__categorykino__iexact='Multfilmlar')
    messages.success(request, "Siz bosh sahifaga keldingiz")
    return render(request, 'home.html', {'kino': kino, 'multfilmlar': multfilmlar})

def NavBar(request):
    return render(request, 'navbar.html')

def movieyear(request, yil):
    movieyil = Movie.objects.filter(categoryyili__categoryyili__iexact=yil)
    return render(request, 'movie_by_year.html', {
        'movieyil': movieyil,
        'yil': yil
    })
 


