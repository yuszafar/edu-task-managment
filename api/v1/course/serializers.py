from rest_framework import serializers
from courses.models import *
from api.v1.user.serializers import StudentListSerializer


class CreateHomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('homework_title', 'homework_file', 'homework_created_time', 'homework_deadline_time',
        'student_group', 'homework_text')


class SendHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = ('homework', 'upload_homework_time', 'submission_homework_file','submission_rating',)


class SubmissionHomeworkList(serializers.ModelSerializer):
    student = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = HomeworkSubmission
        fields = "__all__"
    
    def get_student(self, obj):
        user = obj.student
        serializer_user = StudentListSerializer(user, many=False)

        return serializer_user.data