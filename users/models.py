from django.db import models
from base.models import Base
from django.contrib.auth.models import User


class Adminstator(Base, models.Model):

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choice, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='admin_images', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Teacher(Base, models.Model):
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choice, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='student_images', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Student(Base, models.Model):

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=gender_choice, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='student_images', blank=True, null=True)


    def __str__(self):
        return self.user.username


class StudentGroup(Base, models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length=222, blank=True, null=True)
    owner = models.ForeignKey(User,  on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)