app_name = 'respons_order'
from django.urls import path
from .views import accept_order, reject_order, finish_order

urlpatterns = [
    path('accept-order', accept_order, name="accept_order"),
    path('reject-order', reject_order, name="reject_order"),
    path('finish-order', finish_order, name="finish_order")
]