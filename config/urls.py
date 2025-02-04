from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('rooms/', include('rooms.urls')),
    path('reservations/', include('reservations.urls')),
    path('payments/', include('payments.urls')),
    path('home/', include('home.urls')),
]
