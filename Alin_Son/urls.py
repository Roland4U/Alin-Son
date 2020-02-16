"""Alin_Son URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .views import UserReg as reg
from .views import main, profile
from django.contrib.auth import views as login
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS

    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', main, name='main'),
    path('reg', reg.as_view(), name='reg'),
    path('profile', profile, name='profile'),
    path('login', login.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('exit', login.LogoutView.as_view(template_name='base/exit.html'), name='exit'),
    path('jet_api/', include('jet_django.urls')),
    path('admin/', admin.site.urls),
]

