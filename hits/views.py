from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin

from .forms import HitForm, LoginForm, RegisterForm, HitDetailForm, HitmanDetailForm
from .models import Hit, Hitman


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
            form = HitForm(request.POST, user=user)
            if form.is_valid():
                form.save(created_by=request.user)
                return redirect(
                    reverse_lazy("hits-list") + "?message=succ_hit")
        else:
            form = HitForm(user=user)
        return render(request, 'hits_base.html', {"form": form})
    else:
        raise PermissionDenied


@login_required(login_url=reverse_lazy("login"))
def hit_list_view(request):
    messages = {
        "succ_hit": "The hit was created successfully",
        "succ_up_h": "The hit was updated successfully"
    }
    message = request.GET.get("message", None)
    user = request.user
    if user.is_superuser:
        hits = Hit.objects.all()
    elif user.is_manager:
        hits = Hit.objects.filter(asignee__in=user.hitmen.all()).union(
            user.hits.all())
    else:
        hits = user.hits.all()
    context = {"hits": hits}
    if message is not None:
        context.update({"message": messages.get(message, None)})
    return render(request, "hits_list.html", context)


@login_required(login_url=reverse_lazy("login"))
def hitmen_list_view(request):
    messages = {"succ_hit": "The hitman was updated successfully"}
    message = messages.get(request.GET.get("message", None), None)
    user = request.user
    if user.is_superuser or user.is_manager:
        hitmen = Hitman.objects.all()
        if user.is_manager:
            hitmen = user.hitmen.all()
        context = {"hitmen": hitmen}
        if message is not None:
            context.update({"message": message})
        return render(request, "hitmen_list.html", context)
    else:
        raise PermissionDenied


@login_required(login_url=reverse_lazy("login"))
def hitmen_detail(request, pk: int):
    user = request.user
    if user.is_superuser or user.is_manager:
        hitman = Hitman.objects.get(pk=pk)
        if request.method == "GET":
            form = HitmanDetailForm(user=user, instance=hitman)
        else:
            form = HitmanDetailForm(request.POST, user=user, instance=hitman)
            if form.is_valid():
                form.save()
                return redirect(
                    reverse_lazy("hitmen-list") + "?message=succ_hit")
    else:
        raise PermissionDenied
    return render(
        request, "hitmen_detail.html", {
            "form": form,
            "pk": pk,
            "not_manager": not (user.is_manager or user.is_superuser)
        })


@login_required(login_url=reverse_lazy("login"))
def hit_detail(request, pk: int):
    user = request.user
    hit = Hit.objects.get(pk=pk)
    if user.is_superuser:
        queryset = Hitman.objects.filter(is_active=True).exclude(
            email=user.email)
    else:
        queryset = user.hitmen.all()
    if request.method == "GET":
        form = HitDetailForm(user=user, queryset=queryset, instance=hit)
    else:
        form = HitDetailForm(request.POST,
                             user=user,
                             queryset=queryset,
                             instance=hit)
        if form.is_valid():
            hit_u = form.save()
            print(hit_u)
            return redirect(reverse_lazy("hits-list") + "?message=succ_up_h")
    return render(
        request, "hits_detail.html", {
            "form": form,
            "pk": pk,
            "not_manager": not (user.is_manager or user.is_superuser)
        })


class CustomLoginView(views.LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_field_url = reverse_lazy("login")
    redirect_authenticated_user = True


class RegisterView(CreateView, ModelFormMixin):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")
