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

    def clean(self):
        data = dict(self.data.lists())
        if len(data) != 0 and data['available_time_begin'][0] > data['available_time_end'][0]:
            raise forms.ValidationError({"available_time_begin": "Time end can't precede time begin"})

    def __init__(self, *args, **kwargs):
        super(AddAvailableTimeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == "available_time_begin":
                field.widget.attrs['id'] = 'begin-time-column'
                field.widget.attrs['name'] = 'btime-column'
            else:
                field.widget.attrs['id'] = 'end-time-column'
                field.widget.attrs['name'] = 'etime-column'
