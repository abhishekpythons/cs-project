from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form),
    path('confess/', views.view_form),

]