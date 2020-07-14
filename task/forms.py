#from django import forms
from django.forms import ModelForm
from .models import tasks

class taskForm(ModelForm):
    class Meta:
        model=tasks
        fields="__all__"