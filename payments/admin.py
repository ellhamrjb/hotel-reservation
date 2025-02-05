from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'reservation', 'amount', 'status', 'created_at')  
    list_filter = ('status', 'created_at') 
    search_fields = ('user__username', 'transaction_id', 'reference_id')  
    ordering = ('-created_at',) 