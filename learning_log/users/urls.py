'''
Created on Jan 25, 2023

@author: jcp
'''

"""Defines URL patterns for learning_logs."""
from django.urls import path, include
from . import views 

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]