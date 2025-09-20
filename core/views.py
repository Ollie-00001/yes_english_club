from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RequestForm, ReviewForm
from .models import Request, Review, Service, Teacher, Video, GalleryImage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.utils.dateparse import parse_date

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = Teacher.objects.first()
        context['gallery_images'] = GalleryImage.objects.all()
        return context

class ContactsView(FormView):
    template_name = 'core/contacts.html'
    form_class = RequestForm
    success_url = reverse_lazy('thanks_for_request')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = Teacher.objects.first()
        context["video"] = Video.objects.first()
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Ваша заявка принята!')
        return super().form_valid(form)

class ThanksForRequestView(TemplateView):
    template_name = 'core/thanks_for_request.html'

class RequestView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Request
    template_name = 'core/requests.html'
    context_object_name = 'requests'

    login_url = "login"

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(client_name__icontains=q) |
                Q(email__icontains=q) |
                Q(phone_number__icontains=q) |
                Q(message__icontains=q)
            )

        date_from_raw = self.request.GET.get('date_from')
        date_to_raw = self.request.GET.get('date_to')

        date_from = parse_date(date_from_raw) if date_from_raw else None
        date_to = parse_date(date_to_raw) if date_to_raw else None

        if date_from:
            qs = qs.filter(created_at__date__gte=date_from)
        if date_to:
            qs = qs.filter(created_at__date__lte=date_to)

        sort = self.request.GET.get('sort')
        if sort == 'oldest':
            qs = qs.order_by('created_at')
        else:
            qs = qs.order_by('-created_at')

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['current_get'] = self.request.GET.urlencode()
        return ctx

class RequestDetailsView(DetailView):
    model = Request
    template_name = 'core/request_details.html'
    context_object_name = 'request_obj'

class ReviewsView(ListView):
    model = Review
    template_name = 'core/reviews.html'
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(is_published=True).order_by('-id')
        return context

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'core/create_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('thanks_for_review')

    def form_valid(self, form):
        messages.success(self.request, 'Ваш отзыв был успешно отправлен! Он будет опубликован после проверки.')
        return super().form_valid(form)
    
class ThanksForReviewView(TemplateView):
    template_name = 'core/thanks_for_review.html'

class ServicesView(ListView):
    model = Service
    template_name = 'core/services.html'
    context_object_name = 'services'

class ScheduleView(TemplateView):
    template_name = 'core/schedule.html'