from django.contrib.auth import views, logout as do_logout, login, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from .models import Hitman, Hit
from .forms import LoginForm, RegisterForm, HitForm


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


@login_required(login_url=reverse_lazy("login"))
def hits_create_view(request):
    user = request.user
    if user.is_manager or user.is_superuser:
        if request.method == "POST":
            form = HitForm(request.POST)
            if form.is_valid():
                form.save(created_by=request.user)
        else:
            hitmen = user.hitmen.all() if user.is_manager else Hitman.objects.all(
            ).exclude(user)
            form = HitForm(queryset=hitmen)
        return render(request, 'hits_base.html', {"form": form})
    else:
        return HttpResponseForbidden()


@login_required(login_url=reverse_lazy("login"))
def hit_list_view(request):
    user = request.user
    if user.is_superuser:
        hits = Hit.objects.all()
    elif user.is_manager:
        hits = Hit.objects.filter(asignee__in=user.hitmen)
    else:
        hits = user.hits.all()
    return render(request, "hits_list.html", {"hits": hits})


class CustomLoginView(views.LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_field_url = reverse_lazy("login")
    redirect_authenticated_user = True


class RegisterView(CreateView, ModelFormMixin):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")
