from django.urls import path

from booking.apps import BookingConfig
from booking.views import ServicesListView, ContactsView, ServicesDetailview, ServicesCreateView, ServicesUpdateView, \
   ServicesDeleteView, RestaurantTeamListView, RestaurantTeamDetailview, RestaurantTeamCreateView, \
   RestaurantTeamUpdateView, RestaurantTeamDeleteView, TableListView, TableDetailview, TableCreateView, TableUpdateView, \
   TableDeleteView, ReservationListView, ReservationDetailview, ReservationCreateView, ReservationUpdateView, \
   ReservationDeleteView

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

   path('table/', TableListView.as_view(), name='table_list'),
   path('table/<int:pk>/', TableDetailview.as_view(), name='table_detail'),
   path('table/create/', TableCreateView.as_view(), name='table_create'),
   path('table/<int:pk>/update/', TableUpdateView.as_view(), name='table_update'),
   path('table/<int:pk>/delete/', TableDeleteView.as_view(), name='table_delete'),

   path('reservation/', ReservationListView.as_view(), name='reservation_list'),
   path('reservation/<int:pk>/', ReservationDetailview.as_view(), name='reservation_detail'),
   path('table/<int:pk>/reservation/create/', ReservationCreateView.as_view(), name='reservation_create'),
   path('reservation/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
   path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),

]

