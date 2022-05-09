from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('destination_list/<str:city_name>', views.destination_list, name='destination_list'),
    path('destination_list/destination_details/<str:city_name>', views.destination_details, name='destination_details'),
    path('destination_details/<str:city_name>', views.destination_details, name='destination_details'),
    path('destination_list/destination_details/passenger_detail_def/<str:city_name>',views.passenger_detail_def,name='passenger_detail_def'),
    path('upcoming_trips', views.upcoming_trips, name='upcoming_trips'),
    path('destination_list/destination_details/passenger_detail_def/passenger_detail_def/card_payment', views.card_payment, name='card_payment'),
    path('destination_list/destination_details/passenger_detail_def/passenger_detail_def/otp_verification', views.otp_verification, name='otp_verification'),
    path('destination_list/destination_details/passenger_detail_def/passenger_detail_def/net_payment', views.net_payment, name='net_payment'),

    ]  #function name = index       