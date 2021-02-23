from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form),
    path('dashboard/', views.view_form),

]