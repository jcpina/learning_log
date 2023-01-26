'''
Created on Jan 24, 2023

@author: jcp
'''

# Import the forms module and the model we'll work with
from django import forms
from .models import Topic, Entry

''' Class TopicForm which inherits from forms.ModelForm'''
class TopicForm(forms.ModelForm):
    # the nested Meta class tells django which model to base the form on
    # and which fields to include in the form
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':'Topic:'}  #tells django to not generate a label for the text field
        
''' Class EntryForm. Inherits from forms.ModelForm '''
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}
        labels = {'text':'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}