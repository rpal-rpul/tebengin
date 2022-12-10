from django.urls import path
from .views import *

app_name = 'booking_driver'

urlpatterns = [
    path('', bookingDriver, name="booking-driver"),
    path('create-order', create_order, name="order_driver"),
    path('show-all-driver', show_all_driver, name="show_all_driver"),
    path('show-filtered-driver', show_filtered_driver)
]