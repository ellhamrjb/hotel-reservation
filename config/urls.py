from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path("reservations/", include("reservations.urls", namespace="reservations")),
    path('api/rooms/', include('rooms.urls')),
    path('api/payments/', include('payments.urls')),
]