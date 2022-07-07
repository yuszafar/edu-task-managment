from django.db import models
from base.models import Base
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
class User(AbstractUser):
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choice)
    father_name = models.CharField(max_length=222, blank=True, null=True)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    has_profile = models.BooleanField(default=False)

    def has_profile_true(self):
        self.has_profile = True



class Admin(Base):

    user = models.OneToOneField(User, related_name='owner', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Teacher(Base):
    user = models.OneToOneField(User, related_name='teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Student(Base):


    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class StudentGroup(Base):
    student = models.ManyToManyField(Student, blank=True)
    name = models.CharField(max_length=222, blank=True, null=True)
    owner = models.ForeignKey(Admin,  on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)