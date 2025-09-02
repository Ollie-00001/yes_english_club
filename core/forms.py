from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python
from .models import Request, Review, Service

class RequestForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        region='RU',
        label='Номер телефона',
        widget=forms.TextInput(attrs={'placeholder': 'Например: 81234567890'})
    )

    class Meta:
        model = Request
        fields = ['client_name', 'email', 'phone_number', 'message']
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+71234567890'}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение', 'rows': 5}),
        }

    def clean_phone_number(self):
        number = self.cleaned_data['phone_number']
        if str(number).startswith('8'):
            number = to_python('+7' + str(number)[1:])
        return number

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['client_name', 'text', 'rating']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст отзыва', 'rows': 4}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price']