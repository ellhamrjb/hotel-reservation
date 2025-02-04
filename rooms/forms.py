from django import forms
from .models import Room

class RoomSearchForm(forms.Form):
    room_type = forms.ChoiceField(choices=Room.ROOM_TYPE_CHOICES, required=False)
    num_of_people = forms.IntegerField(min_value=1, required=False)
    available = forms.BooleanField(required=False)
