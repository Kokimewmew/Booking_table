from django.urls import path

from booking.apps import BookingConfig
from booking.views import ServicesListView, ContactsView, ServicesDetailview, ServicesCreateView, ServicesUpdateView, \
   ServicesDeleteView

app_name = BookingConfig.name

urlpatterns = [
   path('', ServicesListView.as_view(), name='main'),
   path('contacts/', ContactsView.as_view(), name='contacts'),
   path('services/<int:pk>/', ServicesDetailview.as_view(), name='services_detail'),
   path('services/create/', ServicesCreateView.as_view(template_name='services_form.html'),  name='services_create'),
   path('services/<int:pk>/update/', ServicesUpdateView.as_view(), name='services_update'),
   path('services/<int:pk>/delete/', ServicesDeleteView.as_view(), name='services_delete'),

]

