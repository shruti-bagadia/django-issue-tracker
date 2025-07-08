from django import forms
from .models import Project , Issue

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'members'] 

        widgets = {
            'members': forms.CheckboxSelectMultiple
        }

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'project', 'status', 'priority', 'assignee', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }
