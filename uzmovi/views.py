from django.shortcuts import render
from django.contrib import messages
from kinolar.models import Movie
def home(request):
    kino = Movie.objects.all()
    messages.success(request, "Siz bosh sahifaga keldingiz")
    return render(request, 'home.html', {'kino': kino})
def NavBar(request):
     return render(request, 'navbar.html')
 


