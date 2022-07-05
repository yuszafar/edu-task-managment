from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from base.models import Base

# Create your models here.

class Admin(Base, models.Model):
    gender_choice = {
        'Male', 'Male'
        'Female', 'Female'
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255,blank=True, null=True)
    phone = models.BigIntegerField()
    avatar = models.ImageField(upload_to='Media/admin-info')
    
