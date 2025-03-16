from django.shortcuts import render
from django.contrib import messages
def home(request):
      # Xabar ko'rsatilganligini tekshiramiz
    messages.success(request, "Siz saytga kirdingiz!")  # Xabar chiqarish
        
    return render(request, 'home.html')

def NavBar(request):
     return render(request, 'navbar.html')
 


