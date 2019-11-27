"""Defines URL pattern for application Polls"""
from django.urls import path
from . import views

#name space help distinguish this urls.py from files in other apps
app_name = 'polls'

urlpatterns=[
    # Home page
    path('', views.index, name='index'),
    # Page that shows all question
    path('questions/', views.questions, name='questions'),
]
