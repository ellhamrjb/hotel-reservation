from django.shortcuts import render, redirect
from django.views import View
from .models import Reservation
from .forms import ReservationForm

class ReserveView(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, "reservations/reservation_form.html", {"form": form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  
        return render(request, "reservations/reservation_form.html", {"form": form})
