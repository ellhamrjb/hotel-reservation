from django.db import models
from users.models import CustomUser
from rooms.models import Room

class Reservation(models.Model):
    MEAL_CHOICES = [
        ('no_meal', 'No Meal'),
        ('breakfast', 'Breakfast'),
        ('half_board', 'Half Board'),
        ('full_board', 'Full Board'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_of_people = models.IntegerField(default=1)
    meal_option = models.CharField(max_length=20, choices=MEAL_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")  
    created_at = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
       
        self.total_price = self.room.price * self.num_of_people
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.user.username} in {self.room.number}"

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
