from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import IntegrityError

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView, DetailView

from booking.forms import ServicesForm, ReservationForm
from booking.models import Services, Table, RestaurantTeam, Reservation, Message


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

            new_message = Message.objects.create(
                name=name,
                phone=phone,
                message=message,
            )

            print(f'You have new message from {new_message.name} {new_message.phone}  {new_message.message}  ')

            return redirect('booking:contacts')


class AdminMessagesView(ListView):
    model = Message
    template_name = 'admin_messages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context

    def post(self, request):
        if request.method == 'POST':
            if 'clear_messages' in request.POST:
                Message.objects.all().delete()
                messages.success(request, 'Все  сообщения  очищены!')
            return redirect('booking:admin_messages')


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
    fields = '__all__'

    def get_success_url(self):
        return reverse('booking:services_detail', args=(self.kwargs.get('pk'),))


class ServicesDeleteView(DeleteView):
    template_name = 'services_delete.html'
    model = Services
    success_url = reverse_lazy('booking:main')


class TableListView(ListView):
    model = Table
    template_name = 'table_list.html'


class TableDetailview(DetailView):
    model = Table
    template_name = 'table_detail.html'


class TableCreateView(CreateView, LoginRequiredMixin):
    model = Table
    fields = '__all__'
    template_name = 'table_form.html'
    success_url = reverse_lazy('booking:table_list')


class TableUpdateView(LoginRequiredMixin, UpdateView):
    model = Table
    template_name = 'table_form.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse('booking:table_detail', args=(self.kwargs.get('pk'),))


class TableDeleteView(DeleteView):
    model = Table
    template_name = 'table_delete.html'
    success_url = reverse_lazy('booking:table_list')


class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user, status__in=[1, 3], end_datetime__gte=timezone.now())
    #

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history_reservation'] = Reservation.objects.filter(end_datetime__lte=timezone.now(),
                                                                    user=self.request.user)
        return context


class ReservationDetailview(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'


class ReservationCreateView(CreateView, LoginRequiredMixin):
    model = Reservation
    form_class = ReservationForm

    template_name = 'reservation_form.html'
    success_url = reverse_lazy('booking:reservation_list')

    def form_valid(self, form):

        try:
            form.instance.user = self.request.user
            table = self.kwargs.get('pk')
            form.instance.table = Table.objects.get(pk=table)
            form.instance.status = 3  # Устанавливаем статус "Ожидание" по умолчанию

            # Получаем данные из формы
            start_date = form.cleaned_data.get('start_date')
            start_time_str = form.cleaned_data.get('start_time')
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            if form.cleaned_data.get('start_time') == '21:00':
                end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=2, minutes=59)).time()
            elif form.cleaned_data.get('start_time') == '22:00':
                end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=1, minutes=59)).time()
            else:
                end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=3, minutes=59)).time()
            end_datetime = datetime.combine(start_date, end_time)
            form.instance.end_datetime = end_datetime

            return super().form_valid(form)
        except IntegrityError as e:
            # Обработка ошибки IntegrityError
            form.add_error(None, 'Этот стол уже забронирован клиентом на это время.')
            return render(self.request, 'reservation_form.html', {'form': form})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user, 'table': self.kwargs.get('pk')})
        return kwargs


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_form.html'

    def form_valid(self, form):
        try:
            start_date = form.cleaned_data.get('start_date')
            start_time_str = form.cleaned_data.get('start_time')
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            if form.cleaned_data.get('start_time') == '21:00':
                end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=2, minutes=59)).time()
            elif form.cleaned_data.get('start_time') == '22:00':
                end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=1, minutes=59)).time()
            else:
                end_time = (datetime.combine(datetime.min, start_time) + timedelta(hours=3, minutes=59)).time()
            end_datetime = datetime.combine(start_date, end_time)
            form.instance.end_datetime = end_datetime
            return super().form_valid(form)
        except IntegrityError as e:
            # Обработка ошибки IntegrityError
            form.add_error(None, 'Этот стол уже забронирован клиентом на это время.')
            return render(self.request, 'reservation_update.html', {'form': form})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user, 'table': self.get_object().table})
        return kwargs

    def get_success_url(self):
        return reverse('booking:reservation_list')


class ReservationDeleteView(DeleteView):
    template_name = 'reservation_delete.html'
    model = Reservation
    success_url = reverse_lazy('booking:reservation_list')


class RestaurantTeamListView(ListView):
    model = RestaurantTeam
    template_name = 'team_list.html'


class RestaurantTeamDetailview(DetailView):
    model = RestaurantTeam
    template_name = 'team_detail.html'


class RestaurantTeamCreateView(CreateView, LoginRequiredMixin):
    fields = '__all__'
    template_name = 'team_form.html'
    model = RestaurantTeam
    success_url = reverse_lazy('booking:team_list')


class RestaurantTeamUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    template_name = 'team_form.html'
    model = RestaurantTeam

    def get_success_url(self):
        return reverse('booking:team_detail', args=(self.kwargs.get('pk'),))


class RestaurantTeamDeleteView(DeleteView):
    template_name = 'team_delete.html'
    model = RestaurantTeam
    success_url = reverse_lazy('booking:team_list')
