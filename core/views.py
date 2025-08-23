from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Request
from django.shortcuts import render

def about(request):
    return render(request, 'core/about.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def order_details(request):
    return render(request, 'core/order_details.html')

class RequestView(TemplateView):
    template_name = 'core/requests.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = Request.objects.all()
        return context

def reviews(request):
    return render(request, 'core/reviews.html')

def services(request):
    return render(request, 'core/services.html')
