from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.permissions import BasePermission

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, default="Default Name")
    last_name = models.CharField(max_length=150, default="Default LastName")
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_guest = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="user_profiles/", null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class IsAdminOrReadOnly(BasePermission):
   
     #only admins can edit the object.
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_staff