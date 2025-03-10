from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not username or not password:
            logger.warning("Foydalanubvchi pasword yoki username kiritilmagan.")
            return render(request, 'login.html', {'erros': 'Iltimos, foydalanuvchi nomi va parolni kiriting.'})
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            auth_login(request, user)
            logger.info(f"Foydalanuvchi {username} saytga kirdi.")
            return redirect('home')
        else:
            logger.warning(f"Login urinishida xatolik: {username}")
            return render(request, 'login.html', {'error': 'Foydalanuvchi nomi yoki parol noto‘g‘ri.'})
    return render(request, 'login.html')


# Python -- Mukaramoy
# Django -- Maqsudbek
# DataBase -- Omadbek
