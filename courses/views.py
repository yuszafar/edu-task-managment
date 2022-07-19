from django.shortcuts import render
from user.models import StudentGroup
from .models import Homework, HomeworkSubmission
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class DetailHomework(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = "hometasks/task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_id'] = StudentGroup.objects.get(id = self.object.id)
        context['homeworks'] = Homework.objects.filter(student_group = self.object.id)
        context['homeworksubmission'] = HomeworkSubmission.objects.filter(homework__in = context['homeworks'], student = self.request.user.student)
        return context

def sendhomework(request):
    list_groups = StudentGroup.objects.all()
    context = {'list_groups':list_groups}
    return render(request, 'hometasks/hometask.html', context)


class CheckHomeworkGroup(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = HomeworkSubmission
    template_name: str = 'users/teacher/checkTaskGroup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checkHomeworkGroupList'] = StudentGroup.objects.filter(groups__teacher = self.request.user.teacher).distinct()
        return context


class CheckHomeworkStudent(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = StudentGroup
    template_name: str = 'users/teacher/checkTaskStudent.html'
    def get_object(self, queryset=None):
        return StudentGroup.objects.get(id = self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['Homework'] = Homework.objects.filter(teacher = self.request.user.teacher, student_group = self.get_object())
            print(context['Homework'])
            return context
        except:
            return {"msg":"error"}