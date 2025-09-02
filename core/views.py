from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RequestForm
from .models import Request, Review, Service

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactsView(FormView):
    template_name = 'core/contacts.html'
    form_class = RequestForm
    success_url = '/thanks_for_request/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

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

class ThanksForRequestView(TemplateView):
    template_name = 'core/thanks_for_request.html'