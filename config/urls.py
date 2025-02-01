from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_view(request):
    return render(request, 'home/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('api/users/', include('users.urls')),
    path('api/reservations/', include('reservations.urls')),
    path('api/rooms/', include('rooms.urls')),
    path('api/payments/', include('payments.urls')),
]
