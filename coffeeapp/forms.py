from django import forms
from .models import Project

class CreateProjectForm(forms.Form):
    name = forms.CharField(label ="Project name", max_length=200)

class CreateTaskForm(forms.Form):
    title = forms.CharField(label ="Task name", max_length=200)
    description = forms.CharField(label = "Text Area", widget=forms.Textarea)
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(), 
        empty_label="Select a Project",
        label="Project",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


