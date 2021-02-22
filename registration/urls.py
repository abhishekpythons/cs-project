from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_form),
    path('register/', views.read_form)
]