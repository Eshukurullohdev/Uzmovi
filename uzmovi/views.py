from django.shortcuts import render
from django.contrib import messages
def home(request):
    if not request.session.get('message_shown'):  # Xabar ko'rsatilganligini tekshiramiz
        messages.success(request, "Siz saytga kirdingiz!")  # Xabar chiqarish
        request.session['message_shown'] = True
    return render(request, 'home.html')

def NavBar(request):
     return render(request, 'navbar.html')
 


