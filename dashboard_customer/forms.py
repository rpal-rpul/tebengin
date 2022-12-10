from django import forms

class AddReviewForm(forms.Form):
    message = forms.CharField(
        label='Message',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'id': 'add-review-message',
                'placeholder': 'Say something to the driver',
                'rows': '10'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(AddAvailableTimeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'add-review-column'
            field.widget.attrs['name'] = 'add-review-column'