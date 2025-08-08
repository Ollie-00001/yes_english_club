from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
    path('orders/', views.orders, name='orders'),
    path('order_details/', views.order_details, name='order_details'),
]