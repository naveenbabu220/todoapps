from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    py = models.ImageField(upload_to ='static/')
    user_name = models.CharField(max_length=62)
    email = models.EmailField()
    password =models.CharField(max_length=20)

    
