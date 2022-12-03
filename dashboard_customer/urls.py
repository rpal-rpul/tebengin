from django.urls import path
from dashboard_customer.views import *

app_name = 'dashboard_customer'

urlpatterns = [
    path('add-review/', add_review),
    path('get-review/', get_review),
    path('get-review-driver/', get_review_driver),
    path('', getCustomerOrder)
]