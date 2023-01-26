'''
Created on Jan 7, 2023

@author: jcp
'''

"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page showing all the topics
    path('topics/', views.topics, name='topics'),
    # Detail for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for users to add a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for users to add new entry to a specific topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for users to edit the entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
]