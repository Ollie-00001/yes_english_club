from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('reviews/', views.ReviewsView.as_view(), name='reviews'),
    path('requests/', views.RequestView.as_view(), name='requests'),
    path('order_details/', views.RequestDetailsView.as_view(), name='order_details'),
    path('thanks_for_request/', views.ThanksForRequestView.as_view(), name='thanks'),
]