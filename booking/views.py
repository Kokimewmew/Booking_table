from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView, DetailView

from booking.forms import ServicesForm, ServicesModeratorForm
from booking.models import Services, Table, RestaurantTeam, Reservation




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
    template_name = 'services_detail.html'

    model = Services


class ServicesCreateView(CreateView, LoginRequiredMixin):
    template_name = 'services_form.html'
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('booking:main')


class ServicesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'services_form.html'
    model = Services

    def get_success_url(self):
        return reverse('booking:services_detail', args=(self.kwargs.get('pk'),))

    def get_form_class(self):
        user = self.request.user
        if user.has_perm(
                "services.can_edit") and user.has_perm(
                "services.can_delete"):
            return ServicesModeratorForm

        raise PermissionDenied


class ServicesDeleteView(DeleteView):
    template_name = 'services_delete.html'
    model = Services
    success_url = reverse_lazy('booking:main')


class TableListView(ListView):
    model = Table


class TableDetailview(DetailView):
    model = Table


class TableCreateView(CreateView, LoginRequiredMixin):
    model = Table
    success_url = reverse_lazy('booking:main')


class TableUpdateView(LoginRequiredMixin, UpdateView):
    model = Table

    def get_success_url(self):
        return reverse('booking:services_detail', args=(self.kwargs.get('pk'),))


class TableDeleteView(DeleteView):
    template_name = 'booking/services_delete.html'
    model = Table
    success_url = reverse_lazy('booking:main')


class ReservationListView(ListView):
    model = Reservation


class ReservationDetailview(DetailView):
    model = Reservation


class ReservationCreateView(CreateView, LoginRequiredMixin):
    model = Reservation
    success_url = reverse_lazy('booking:main')


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation

    def get_success_url(self):
        return reverse('booking:services_detail', args=(self.kwargs.get('pk'),))


class ReservationDeleteView(DeleteView):
    template_name = 'booking/services_delete.html'
    model = Reservation
    success_url = reverse_lazy('booking:main')


class RestaurantTeamListView(ListView):
    model = RestaurantTeam
    template_name = 'team_list.html'


class RestaurantTeamDetailview(DetailView):
    model = RestaurantTeam
    template_name = 'team_detail.html'



class RestaurantTeamCreateView(CreateView, LoginRequiredMixin):
    model = RestaurantTeam
    success_url = reverse_lazy('booking:main')


class RestaurantTeamUpdateView(LoginRequiredMixin, UpdateView):
    model = RestaurantTeam
    template_name = 'team_form.html'


    def get_success_url(self):
        return reverse('booking:services_detail', args=(self.kwargs.get('pk'),))


class RestaurantTeamDeleteView(DeleteView):
    template_name = 'booking/services_delete.html'
    model = RestaurantTeam
    success_url = reverse_lazy('booking:main')
