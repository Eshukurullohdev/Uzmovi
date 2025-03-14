from django.contrib import admin
from django.urls import path, include  # include django.urls ichidan olinishi kerak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uzmovi.urls')),
    path('auth/', include('Authentication.urls')),
]
