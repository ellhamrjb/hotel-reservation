from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    ]

    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()  # How many people can stay in this room
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return f"Room {self.number} - {self.get_room_type_display()}"
