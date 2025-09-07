from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('thanks_for_request/', views.ThanksForRequestView.as_view(), name='thanks_for_request'),
    path('reviews/', views.ReviewsView.as_view(), name='reviews'),
    path('reviews/create/', views.ReviewCreateView.as_view(), name='create_review'),
    path('thanks_for_review/', views.ThanksForReviewView.as_view(), name='thanks_for_review'),
    path('requests/', views.RequestView.as_view(), name='requests'),
    path('order_details/', views.RequestDetailsView.as_view(), name='order_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)