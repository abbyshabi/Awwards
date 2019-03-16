from django import forms
from .models import Project,Review,Comments
from django.core import validators


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['poster']
