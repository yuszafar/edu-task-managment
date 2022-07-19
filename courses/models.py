from users.models import *
from base.models import Base
import os
from django.core.validators import FileExtensionValidator
from datetime import datetime
import pytz
from rest_framework.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



def deadline_time(value):

    if value < datetime.now(pytz.utc):
        raise ValidationError("Error Time")



class Homework(Base):
    homework_title = models.CharField(max_length=255)
    homework_text = models.TextField(blank=True)
    homework_file = models.FileField(upload_to='homeworks/questions/group/')
    homework_created_time = models.DateTimeField(auto_now_add=True)
    homework_deadline_time = models.DateTimeField(null=True, validators=[deadline_time])
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True)
    student_group = models.ManyToManyField(StudentGroup)
    student = models.ManyToManyField(Student, blank=True)
    def filename(self):
        return os.path.basename(self.homework_file.name)



class HomeworkSubmission(Base):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    upload_homework_time = models.DateTimeField(auto_now_add=True)
    submission_homework_file = models.FileField(upload_to='homeworks/answers/', blank=True)
    submission_rating = models.IntegerField(blank=True, validators=[MaxValueValidator(5), MinValueValidator(0)])
    is_answered = models.BooleanField(default=False)
    def filename(self):
        return os.path.basename(self.submission_homework_file.name)