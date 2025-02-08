from django.db import models
from django.conf import settings
from rooms.models import Room

class MealPlan(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Meal Plan"
        verbose_name_plural = "Meal Plans"

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.id} - {self.user.username} ({self.status})"

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
