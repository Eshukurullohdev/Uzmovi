from django.urls import path
from .views import *


urlpatterns = [
    path('qoidalar/', Qoida, name='qoidalar'),
]
