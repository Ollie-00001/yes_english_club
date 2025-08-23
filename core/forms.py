from django import forms
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField
from phonenumber_field.phonenumber import to_python
from .models import Request, Review

class RequestForm(forms.ModelForm):
    phone_number = FormPhoneNumberField(region='RU')

    class Meta:
        model = Request
        fields = ['client_name', 'email', 'phone_number', 'message']

    def clean_phone_number(self):
        number = self.cleaned_data['phone_number']
        if str(number).startswith('8'):
            number = to_python('+7' + str(number)[1:])
        return number

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['client_name', 'text']