from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):
    template_name: str = "users/login_simple.html"
    def get_success_url(self):
        if hasattr(self.request.user, 'student'):
            success_url = reverse_lazy("studentProfile")
        elif hasattr(self.request.user, 'teacher'):
            success_url = reverse_lazy("teacherProfile")
        elif hasattr(self.request.user, 'owner'):
            success_url = reverse_lazy("adminProfile")
        return success_url