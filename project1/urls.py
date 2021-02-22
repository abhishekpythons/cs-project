"""project1 URL Configuration

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
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def show_license(request):
    return render(request, 'license.html')
def contact(request):
    return render(request, 'contact.html')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('about/', about),
    path('license/', show_license),
    path('contact', contact),
    path('login/', include('login.urls')),
    path('registration/', include('registration.urls')),

]
