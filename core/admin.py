from django.contrib import admin
from .models import Request, Review, Service

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'email', 'phone_number', 'created_at']
    search_fields = ['client_name', 'email', 'phone_number']
    list_filter = ['created_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'text']
    search_fields = ['client_name', 'text']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']