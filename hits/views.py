from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm


class CustomLoginView(views.LoginView):
    template_name = "login.html"
    authentication_form = LoginForm


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
