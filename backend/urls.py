from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uzmovi.urls')),
    path('auth/', include('Authentication.urls')),
    path('qoidalar/', include('qoidalar.urls')),
]
