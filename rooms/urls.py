from django.urls import path
from .views import RoomListView, RoomTypeListView, RoomDetailView,RoomPagination
from . import views

urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
]
