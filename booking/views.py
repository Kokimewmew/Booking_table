from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView, DetailView

from booking.forms import ServicesForm
from booking.models import Services


class ServicesListView(ListView):
    model = Services
    template_name = "base.html"


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            print(f'You have new message from {name} ({phone}): {message}')
        return render(request, template_name='contacts.html')


class ServicesDetailview(DetailView):
    model = Services


class ServicesCreateView(CreateView, LoginRequiredMixin):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('booking:main')


class ServicesUpdateView(LoginRequiredMixin, UpdateView):
    model = Services

    def get_success_url(self):
        return reverse('booking:services_detail', args=(self.kwargs.get('pk'),))


class ServicesDeleteView(DeleteView):
    template_name = 'booking/services_delete.html'
    model = Services
    success_url = reverse_lazy('booking:main')
