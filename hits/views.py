from django.contrib.auth import views, logout as do_logout, login, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm


def logout(request):
    do_logout(request)
    return redirect("/")


def signup_view(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            print(form.errors)
    return render(request, 'register.html', {'form': form})


class CustomLoginView(views.LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_field_url = reverse_lazy("login")
    redirect_authenticated_user = True


class RegisterView(CreateView, ModelFormMixin):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")
