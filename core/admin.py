from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'email', 'phone_number', 'created_at']
    search_fields = ['client_name', 'email', 'phone_number']
    list_filter = ['created_at']