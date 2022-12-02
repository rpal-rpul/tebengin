from django.urls import path
from . import views

app_name = 'dashboard_customer'

urlpatterns = [
    path('add-review/', views.add_review),
    path('get-review/', views.get_review)
]