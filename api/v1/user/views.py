from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from user.models import *
from rest_framework.response import Response
from rest_framework import status

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class StudentUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer




class StudentGroupCreate(generics.CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer



class TeacherCreate(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer


class TeacherUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSerializer

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentGroupList(APIView):
    serializer_class = StudentGroupListSerializer

    def get(self, request):
        user = request.user.id
        group = StudentGroup.objects.filter(owner = user)

        serializer = self.serializer_class(group, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class StudentGroupDetailList(APIView):

    def get(self, request, pk):

        group = StudentGroup.objects.filter(id = pk)
        serializer = StudentGroupListSerializer(group, many=True)
        return Response(serializer.data)