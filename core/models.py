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
    
class Review(models.Model):
    text = models.TextField(max_length=500)
    client_name = models.CharField(max_length=100, blank=True)

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title