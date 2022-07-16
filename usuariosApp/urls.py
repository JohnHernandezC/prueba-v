from django.urls import path
from .views import *

urlpatterns = [
    path('',Inicio,name='index-principal'),
]