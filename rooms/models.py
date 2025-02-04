from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Room Type"
        verbose_name_plural = "Room Types"

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="rooms")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField()
    images = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.room_type.name} - {self.room_number}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
