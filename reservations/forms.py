from django import forms
from .models import Reservation
from datetime import timezone

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'check_in', 'check_out', 'num_of_people', 'meal_option']

    def clean_check_in(self):
        check_in = self.cleaned_data.get('check_in')
        if check_in < timezone.now().date():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        return check_in

    def clean_check_out(self):
        check_out = self.cleaned_data.get('check_out')
        if check_out <= self.cleaned_data.get('check_in'):
            raise forms.ValidationError("Check-out date must be after check-in date.")
        return check_out
