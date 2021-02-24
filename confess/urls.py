from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_form),
    path('send_confession/', views.read_form)
]