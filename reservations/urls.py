from django.urls import path
from .views import ReserveView

app_name = "reservations"

urlpatterns = [
    path("reserve/", ReserveView.as_view(), name="reserve"),
]
