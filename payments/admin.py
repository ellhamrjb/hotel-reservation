from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'amount', 'method', 'status', 'created_at')
    list_filter = ('status', 'method')
    search_fields = ('reservation__user__username', 'transaction_id')
