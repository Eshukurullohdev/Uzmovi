from django.urls import path
from . views import DetailMovie
urlpatterns = [
    path('movie/<int:movie_id>/', DetailMovie, name='detail_movie'),
]
