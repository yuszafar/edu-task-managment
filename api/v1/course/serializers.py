from rest_framework import serializers
from courses.models import *
from datetime import datetime


class CreateHomeworkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Homework
        fields = ('homework_title', 'homework_file', 'homework_created_time', 'homework_deadline_time',
        'student_group','teacher',)



class SendHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = ('homework', 'student', 'upload_homework_time', 'submission_homework_file','submission_rating',)


class CreateHomeworkStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkStudent
        fields = ('student', 'teacher', 'homework_title', 'homework_text', 'homework_file',
            'homework_created_time', 'homework_deadline_time',)


class AnswerHomeworkStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkAnswer
        fields = ('homework_task', 'student', 'upload_homework_time', 'answer_file', 'answer_rating',)