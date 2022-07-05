from django.db import models
from base.models import Base
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choice)
    father_name = models.CharField(max_length=222, blank=True, null=True)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)



class Admin(Base, models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Teacher(Base, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Student(Base, models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class StudentGroup(Base, models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length=222, blank=True, null=True)
    owner = models.ForeignKey(User,  on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)