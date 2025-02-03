from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'room', 'check_in_date', 'check_out_date', 'num_of_people', 'meal_option']

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['check_in_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['check_out_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['meal_option'].widget = forms.Select(choices=Reservation.MEAL_CHOICES)
