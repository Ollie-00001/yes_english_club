from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python
from .models import Request, Review, Service

class RequestForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        region='RU',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Телефон',
            'class': 'form-control',
            'autocomplete': 'tel'
        })
    )

    class Meta:
        model = Request
        fields = ['client_name', 'email', 'phone_number', 'message']
        labels = {
            'client_name': '',
            'email': '',
            'phone_number': '',
            'message': '',
        }
        widgets = {
            'client_name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'form-control',
                'autocomplete': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'E-mail',
                'class': 'form-control',
                'autocomplete': 'email'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Сообщение',
                'rows': 5,
                'class': 'form-control',
                'autocomplete': 'off'
            }),
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
        labels = {
            'client_name': '',
            'text': '',
            'rating': '',
        }
        widgets = {
            'client_name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Ваш отзыв',
                'rows': 5,
                'class': 'form-control'
            }),
            'rating': forms.Select(
                choices=[(i, str(i)) for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price']