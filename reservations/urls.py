from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ReservationCreateView.as_view(), name='reservation-create'),
    path('list/', views.ReservationListView.as_view(), name='reservation-list'),
]
