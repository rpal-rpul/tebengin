from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('registerRole/', views.registerPenggunaRole, name='registerRole'),
    path('registerDriver/', views.register_driver, name='registerDriver'),
    path('registerCustomer/', views.register_customer, name='registerCustomer'),
]