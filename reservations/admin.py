from django.contrib import admin
from .models import Reservation, MealPlan

class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
    ordering = ('name',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'guests', 'meal_plan', 'total_price', 'status')
    list_filter = ('status', 'check_in', 'check_out')
    search_fields = ('user__username', 'room__room_number')
    ordering = ('-check_in',)

admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(Reservation, ReservationAdmin)
