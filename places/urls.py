from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('places',views.place, name="place")] 