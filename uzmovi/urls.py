from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
     path('movies/year/<str:yil>/', movieyear, name='movie_by_year'),
]
