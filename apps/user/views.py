from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, RegisterForm
# Create your views here.


class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_success_url(self):
        url = self.request.POST.get('next')
        return url or super(Login, self).get_success_url()


class Logout(LogoutView):
    pass
