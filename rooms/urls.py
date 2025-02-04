from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room-list'),
    path('<int:pk>/', views.room_detail, name='room-detail'),
]
