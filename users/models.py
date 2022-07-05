from django.db import models
from base.models import Base
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choice)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    has_profile = models.BooleanField(default=False)

    def has_profile_true(self):
        self.has_profile = True



class Admin(Base):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')


    def __str__(self):
        return self.user.username

class Teacher(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    position = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.user.username
    

class Student(Base):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    education_start_date = models.DateField()



    def __str__(self):
        return self.user.username


class StudentGroup(Base):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User,  on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)