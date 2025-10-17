from django import forms
from .models import Developer, Project

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'email', 'age']  
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'developer']
        
    
