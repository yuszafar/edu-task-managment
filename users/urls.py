from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('student-table/', studentGroup, name='student-group'),
    path('student-list/<int:pk>', studentList, name='student-list'),
    path('teacher-list/', teacherList, name='teacher-list'),
    path('groups/', groups, name='groups'),
    path('tasks/', tasks, name='tasks'),
    path('hometask/', hometask, name='hometask'),
]
