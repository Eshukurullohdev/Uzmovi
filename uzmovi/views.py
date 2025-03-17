from django.shortcuts import render
from django.contrib import messages
def home(request):
    messages.success(request, "Siz bosh sahifaga keldingiz")
    return render(request, 'home.html')
def NavBar(request):
     return render(request, 'navbar.html')
 


