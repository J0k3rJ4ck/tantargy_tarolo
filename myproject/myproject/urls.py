"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import SignUp
from .views import main
from .views import CustomLoginView


urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('register/', views.register, name='register'),
    #path('main/', views.main, name='main'),
   # path('main/', main, name='main'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('main/', views.main_view, name='main'),
    path('create_tantargy/', views.create_tantargy, name='create_tantargy'),
    path('create_kovetelmeny/', views.create_kovetelmeny, name='create_kovetelmeny'),



]
