from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Request, Review, Service
from django.shortcuts import render

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactsView(TemplateView):
    template_name = 'core/contacts.html'

class RequestDetailsView(TemplateView):
    template_name = 'core/request_details.html'

class RequestView(TemplateView):
    template_name = 'core/requests.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Request.objects.all()
        return context

class ReviewsView(TemplateView):
    template_name = 'core/reviews.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context

class ServicesView(TemplateView):
    template_name = 'core/services.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context