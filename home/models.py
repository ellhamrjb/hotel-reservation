from django.db import models

class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_image = models.ImageField(upload_to='home_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Content"
        verbose_name_plural = "Home Contents"

class HotelInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hotel Info"
        verbose_name_plural = "Hotel Info"
