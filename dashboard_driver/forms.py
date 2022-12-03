from django import forms

from authentication.models import AvailableDateTime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class AddAvailableTimeForm(forms.ModelForm):
    class Meta:
        model = AvailableDateTime
        fields = '__all__'
        widgets = {
            'available_time_begin': DateTimeInput(),
            'available_time_end': DateTimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AddAvailableTimeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['type'] = 'text'
