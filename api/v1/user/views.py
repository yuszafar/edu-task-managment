
from urllib import request
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from users.models import *
from rest_framework.response import Response
from rest_framework import status

class StudentCreate(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentCreateSerializer

class StudentGroupCreate(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer

class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentGroupList(generics.ListAPIView):
    serializer_class = StudentGroupListSerializer

    def get_queryset(self):

        if self.request.user.id:
            owner = self.request.user.id
            return StudentGroup.objects.filter(owner = owner)
        
        else:
            return StudentGroup.objects.all()


class StudentGroupDetailList(APIView):

    def get(self, request, pk):

        group = StudentGroup.objects.filter(id = pk)
        serializer = StudentGroupListSerializer(group, many=True)
        return Response(serializer.data)