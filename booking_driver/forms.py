from django import forms
from dashboard_driver.models import Order

class BookingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pickup_location', 'destination_location', 'distance']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['type'] = 'text'
