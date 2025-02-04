from django.db import models
from reservations.models import Reservation

class Payment(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE,default=1)
    payment_id = models.CharField(max_length=100, unique=True,default=1)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
