"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from web import views as web_views
urlpatterns = [
    path('', web_views.index, name='index'),
    path('acerca/', web_views.about, name='about'),
    path('register/', web_views.register, name='register'),
    path('login/', web_views.log_in, name='log_in'),
    path('logout/',web_views.log_out,name='log_out'),
    path('bienvenido/', web_views.welcome, name='welcome'),
    path('contacto/', web_views.contact, name='contact'),
    path('contacto/exito', web_views.success, name='success'),
    path('admin/', admin.site.urls),
    
]
