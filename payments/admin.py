from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'payment_id', 'status', 'amount', 'transaction_date')
    list_filter = ('status', 'transaction_date')
    search_fields = ('payment_id', 'reservation__user__username')
    ordering = ('-transaction_date',)

admin.site.register(Payment, PaymentAdmin)
