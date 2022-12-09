from django.urls import path
from .views import profile, change_password, update_data

app_name = 'profilepage'

urlpatterns = [
    path('', profile, name="profile-page"),
    path('change-password/', change_password, name="password-change"),
    path('ajax/update/', update_data, name="ajax")
]
