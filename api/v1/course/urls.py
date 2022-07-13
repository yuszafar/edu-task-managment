from django.urls import path
from .views import CreateHomework, SendHomework, HomeworkStudents, AnswerStudents

urlpatterns = [
    path('homework/create/', CreateHomework.as_view()),
    path('homework/answer/', SendHomework.as_view()),
    path('homework/student/create/', HomeworkStudents.as_view()),
    path('homework/student/answer/', AnswerStudents.as_view())
]