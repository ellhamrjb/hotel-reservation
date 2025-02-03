from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in_date', 'check_out_date', 'num_of_people', 'meal_option', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'check_in_date', 'check_out_date')
    search_fields = ('user__username', 'room__number')

admin.site.register(Reservation, ReservationAdmin)
