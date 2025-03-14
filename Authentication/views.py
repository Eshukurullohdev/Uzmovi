from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.shortcuts import render, redirect
import logging

logger = logging.getLogger(__name__)  
User = get_user_model()  # Django user modelini olish

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        next_url = request.GET.get('next', 'home')  # Foydalanuvchini oldingi sahifasiga yo‘naltirish

        if not username:
            logger.warning('Foydalanuvchi nomi kiritilmagan.')
            return render(request, 'login.html', {'error': 'Iltimos, foydalanuvchi nomini kiriting.'})
        
        try:
            user = User.objects.get(username=username)  # Foydalanuvchini username bo‘yicha tekshirish
            if user.is_superuser:  # Agar superuser bo‘lsa, parol tekshirilmaydi
                auth_login(request, user)
                logger.info(f"Superuser {username} tizimga kirdi.")
                return redirect(next_url)
            else:
                if not password:
                    logger.warning(f"{username} parolni kiritmadi.")
                    return render(request, 'login.html', {'error': 'Iltimos, parolni kiriting.'})
                
                user = authenticate(request, username=username, password=password)  # Oddiy foydalanuvchi uchun autentifikatsiya
                if user:
                    auth_login(request, user)
                    logger.info(f"Foydalanuvchi {username} tizimga kirdi.")
                    print('ishladi')
                    return redirect('/home/')
                else:
                    logger.warning(f"Login urunishda xatolik: {username}")
                    return render(request, 'login.html', {'error': 'Foydalanuvchi nomi yoki parol noto‘g‘ri.'})
        except User.DoesNotExist:
            logger.warning(f"Foydalanuvchi topilmadi: {username}")
            return render(request, 'login.html', {'error': 'Bunday foydalanuvchi mavjud emas.'})

    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def contact(request):
    return render(request, 'contact.html')
def regulation(request):
    return render(request, 'regulation.html')