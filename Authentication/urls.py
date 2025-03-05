from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login, name='register'),
    
]