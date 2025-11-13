from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import Developer, Project


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise ValidationError("Name is required.")

        if len(name) < 3:
            raise ValidationError("Name must be at least 3 characters long.")

        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise ValidationError("Email is required.")

        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if email and "spam" in email:
            self.add_error("email", "Email cannot contain 'spam'.")

        return cleaned_data



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if not title:
            raise ValidationError("Project title is required.")

        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters.")

        return title


    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        developers = cleaned_data.get('developers')

        if not description:
            self.add_error("description", "Description cannot be empty.")

        if start and end and end < start:
            self.add_error("end_date", "End date must be after start date.")

        if not developers or developers.count() == 0:
            self.add_error("developers", "You must assign at least one developer to the project.")

        return cleaned_data


