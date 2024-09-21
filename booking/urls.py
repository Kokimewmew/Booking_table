from django.urls import path

from booking.apps import BookingConfig
from booking.views import ServicesListView, ContactsView, ServicesDetailview, ServicesCreateView, ServicesUpdateView, \
   ServicesDeleteView, RestaurantTeamListView, RestaurantTeamDetailview, RestaurantTeamCreateView, \
   RestaurantTeamUpdateView, RestaurantTeamDeleteView

app_name = BookingConfig.name

urlpatterns = [
   path('', ServicesListView.as_view(), name='main'),
   path('contacts/', ContactsView.as_view(), name='contacts'),


   path('services/<int:pk>/', ServicesDetailview.as_view(), name='services_detail'),
   path('services/create/', ServicesCreateView.as_view(),  name='services_create'),
   path('services/<int:pk>/update/', ServicesUpdateView.as_view(), name='services_update'),
   path('services/<int:pk>/delete/', ServicesDeleteView.as_view(), name='services_delete'),


   path('team/', RestaurantTeamListView.as_view(), name='team_list'),
   path('team/<int:pk>/', RestaurantTeamDetailview.as_view(), name='team_detail'),
   path('team/create/', RestaurantTeamCreateView.as_view(), name='team_create'),
   path('team/<int:pk>/update/', RestaurantTeamUpdateView.as_view(), name='team_update'),
   path('team/<int:pk>/delete/', RestaurantTeamDeleteView.as_view(), name='team_delete'),

]

