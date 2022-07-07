from urllib import request
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from users.models import *
from rest_framework.response import Response
from rest_framework import status

class StudentCreate(APIView):
    
    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if  self.request.POST.get('group'):
                studentGroup = StudentGroup.objects.filter(id= self.request.POST.get('group'))[0]
                student = Student.objects.filter(user__username = serializer.data['username'])[0]
                studentGroup.student.add(student.id)
                studentGroup.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

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