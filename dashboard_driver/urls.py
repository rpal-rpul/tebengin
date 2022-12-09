from django.urls import path
from .views import *

app_name = 'dashboard_driver'

urlpatterns = [
    path('add-available-time', addAvailableTime, name='addAvailableTime'),
    path('', getDriverOrder, name='getDriverOrder'),
]