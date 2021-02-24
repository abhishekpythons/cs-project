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
import mysql.connector
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def logo(request):
    return render(request, 'CONFESSINATOR_LOGO.svg')


def about(request):
    return render(request, 'about.html')


def show_license(request):
    return render(request, 'license.html')


def contact(request):
    return render(request, 'contact.html')


def reset_database(request):
    conn = mysql.connector.connect(host="sql12.freemysqlhosting.net", user='sql12394795', password='u4Z2pxHSqk',
                                   database='sql12394795')
    cur = conn.cursor()
    cur.execute("delete from user_details")
    conn.commit()
    return render(request, 'index.html', {'type': 'database', 'color': 'indigo', 'message': 'database resets successfully'})


urlpatterns = [
    path('', home),
    path('home/', home),
    path('logo/', logo),
    path('admin/', admin.site.urls),
    path('about/', about),
    path('license/', show_license),
    path('contact', contact),
    path('login/', include('login.urls')),
    path('registration/', include('registration.urls')),
    path('login/confess/', include('confess.urls')),
    path('admin/clear', reset_database)
]
