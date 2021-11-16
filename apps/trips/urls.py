from django.urls import path

from .views import TripView, CreateTripView

app_name = 'asso'

urlpatterns = [
    path('list/', TripView.as_view({'get': 'list'}), name='trip-list'),
    path('<uuid:trip_id>/', TripView.as_view({'get': 'retrieve', 'put': 'update'}), name='trip-detail'),
    path('create/', CreateTripView.as_view(), name='trip-create'),
]