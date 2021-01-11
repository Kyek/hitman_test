from django.contrib.auth import views, logout as do_logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm


def logout(request):
    do_logout(request)
    return redirect("/")


class CustomLoginView(views.LoginView):
    template_name = "login.html"
    authentication_form = LoginForm


class RegisterView(CreateView, ModelFormMixin):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")
