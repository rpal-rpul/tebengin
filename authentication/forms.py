from django import forms
from django.contrib.auth.forms import UserCreationForm

class ChoiceRoleForm(forms.Form):
    CHOICES=[
        ('Driver','Driver'),
        ('Customer','Customer')]
    Role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class DriverRoleForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=20)


class CustomerRoleForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
        