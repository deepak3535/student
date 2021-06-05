from django import urls
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('student',views.student),
    path('count',views.count)
]