from django.urls import path
from . views import DetailMovie
urlpatterns = [
    path('detail/', DetailMovie, name='detail'),
]
