from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    
    class Meta:
        model = Room
        fields = ['name', 'description', 'price_per_night', 'available', 'image']
