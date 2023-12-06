from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,default=" ")
    last_name = models.CharField(max_length=50,default=" ")
    address = models.CharField(max_length=100,default=" ")
    phone_number = models.CharField(max_length=15,default=" ")
    class Meta:
        app_label = 'users'
    def __str__(self):
        return f"{self.user.username} Profile"
