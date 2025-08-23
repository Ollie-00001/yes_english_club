from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Request(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(region='RU', null=True, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} ({self.created_at.strftime('%d.%m %H:%M')})"
