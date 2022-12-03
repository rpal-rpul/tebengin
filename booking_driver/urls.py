from django.urls import path
from .views import *

app_name = 'booking_driver'

urlpatterns = [
    path('', bookingDriver, name='bookingDriver')
]