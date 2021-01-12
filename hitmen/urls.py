"""hitmen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from hits.views import (CustomLoginView, hit_list_view, hits_create_view,
                        logout, signup_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", CustomLoginView.as_view(), name="login"),
    path("register", signup_view, name="register"),
    path("logout", logout, name="logout"),
    path("hits/create", hits_create_view, name="hits-create"),
    path("hits/", hit_list_view, name="hits-list"),
]
