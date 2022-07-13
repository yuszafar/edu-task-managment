from .serializers import (
    CreateHomeworkSerializer,
    CreateHomeworkStudentSerializer,
    SendHomeworkSerializer,
    CreateHomeworkSerializer,
    AnswerHomeworkStudentSerializer,
    )
from rest_framework.generics import CreateAPIView
from courses.models import (
    Homework, 
    HomeworkSubmission,
    HomeworkAnswer,
    HomeworkStudent
    )
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateHomework(CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = CreateHomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(teacher = self.request.user.teacher)


class SendHomework(CreateAPIView):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = SendHomeworkSerializer


class HomeworkStudents(CreateAPIView):
    queryset = HomeworkStudent.objects.all()
    serializer_class = CreateHomeworkStudentSerializer

    def perform_create(self, serializer):
        serializer.save(teacher = self.request.user.teacher)

class AnswerStudents(CreateAPIView):
    queryset = HomeworkAnswer.objects.all()
    serializer_class = AnswerHomeworkStudentSerializer