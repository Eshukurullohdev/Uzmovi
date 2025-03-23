from django.contrib import admin
from django.urls import path, include  # include django.urls ichidan olinishi kerak
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uzmovi.urls')),
    path('auth/', include('Authentication.urls')),
    path('kinolar/', include('kinolar.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
