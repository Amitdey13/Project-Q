from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.logIn, name='nquora-login'),
    path('register/', views.register, name='nquora-register'),
]
