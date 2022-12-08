from django import forms
from authentication.models import Pengguna,Driver,Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'images', 'destination', 'distance_from_campus')
    
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'email', 'images', 'destination', 'distance_from_campus', 'phone_number', 'fee_per_km', 'license_plate')