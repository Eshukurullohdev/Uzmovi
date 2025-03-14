from django.urls import path
from .views import Qoida


urlpatterns = [
    path('qoidalar/', Qoida, name='qoidalar'),
]
