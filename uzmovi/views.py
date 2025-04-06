from django.shortcuts import render
from django.contrib import messages
from kinolar.models import Movie
def home(request):
    kino = Movie.objects.all()
    multfilmalr = Movie.objects.filter(categorykinolar__categorykino__iexact='Multfilmlar')
    messages.success(request, "Siz bosh sahifaga keldingiz")
    return render(request, 'home.html', {'kino': kino, 'multfilmalr': multfilmalr})
def NavBar(request):
     return render(request, 'navbar.html')
 


