from django.db import models
from user.models import *
from base.models import Base
import os
from django.core.validators import FileExtensionValidator



class Homework(Base):
    homework_title = models.CharField(max_length=255)
    homework_file = models.FileField(upload_to='homeworks/questions/')
    homework_created_time = models.DateTimeField(auto_now_add=True)
    homework_deadline_time = models.DateTimeField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    student_group = models.ManyToManyField(StudentGroup)

    def filename(self):
        return os.path.basename(self.homework_file.name)

class HomeworkSubmission(Base):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    upload_homework_time = models.DateTimeField(auto_now_add=True)
    submission_homework_file = models.FileField(upload_to='homeworks/answers/', blank=True, 
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx", "ppt"])])
    submission_rating = models.FloatField(blank=True)

    def filename(self):
        return os.path.basename(self.submission_homework_file.name)