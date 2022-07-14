from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')


def studentGroup(request):
    groups = StudentGroup.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'users/student/studentGroup_list.html', context)

def studentList(request, pk):
    student = StudentGroup.objects.filter(id = pk)
    context = {
        'student':student,
        'pk':pk
    }
    return render(request, 'users/student/studentList.html', context)

def teacherList(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers':teachers,
    }
    return render(request, 'users/teacher/teacherList.html', context)

def groups(request):
    groups = StudentGroup.objects.all()
    context = {
        'groups':groups
    }
    return render(request, 'users/student/groups.html', context)

def tasks(request):
    return render(request, 'users/student/task.html')

def hometask(request):
    return render(request, 'hometasks/hometask.html')