from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
import logging

logger = logging.getLogger(__name__)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            logger.warning("Foydalanuvchi yoki parol kiritilmagan.")
            return render(request, 'login.html', {'error': 'Iltimos, foydalanuvchi nomi va parolni kiriting.'})

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            logger.info(f"Foydalanuvchi {username} tizimga kirdi.")
            return redirect('home')
        else:
            logger.warning(f"Login urinishida xatolik: {username}")
            return render(request, 'login.html', {'error': 'Foydalanuvchi nomi yoki parol noto‘g‘ri.'})

    return render(request, 'login.html')
