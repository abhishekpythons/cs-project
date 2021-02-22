from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form),
    path('submit_form/', views.view_form),

]