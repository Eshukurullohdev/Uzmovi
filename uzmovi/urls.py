from django.urls import path
from .views import *

urlpatterns = [
    path("home/", BaseView.as_view(), name='home')
]
