from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.about, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
    path('requests/', views.RequestView.as_view(), name='requests'),
    path('order_details/', views.order_details, name='order_details'),
]