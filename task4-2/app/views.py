from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm


class DeveloperListView(ListView):
    model = Developer
    template_name = 'developer_list.html'


class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'developer_detail.html'


class DeveloperCreateView(CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'developer_form.html'
    success_url = reverse_lazy('developer_list')

    def form_valid(self, form):
        try:
            messages.success(self.request, "Developer created successfully.")
            return super().form_valid(form)
        except Exception as e:
            form.add_error(None, str(e))
            messages.error(self.request, "Error creating developer.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form. Please correct the errors.")
        return super().form_invalid(form)


class DeveloperUpdateView(UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'developer_form.html'
    success_url = reverse_lazy('developer_list')

    def form_valid(self, form):
        try:
            messages.success(self.request, "Developer updated successfully.")
            return super().form_valid(form)
        except Exception as e:
            form.add_error(None, str(e))
            messages.error(self.request, "Error updating developer.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form. Please fix the issues.")
        return super().form_invalid(form)


class DeveloperDeleteView(DeleteView):
    model = Developer
    template_name = 'developer_confirm_delete.html'
    success_url = reverse_lazy('developer_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Developer deleted successfully.")
        return super().delete(request, *args, **kwargs)



class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        try:
            messages.success(self.request, "Project created successfully.")
            return super().form_valid(form)
        except Exception as e:
            form.add_error(None, str(e))
            messages.error(self.request, "Error creating project.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form. Please fix the errors.")
        return super().form_invalid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        try:
            messages.success(self.request, "Project updated successfully.")
            return super().form_valid(form)
        except Exception as e:
            form.add_error(None, str(e))
            messages.error(self.request, "Error updating project.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form data.")
        return super().form_invalid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Project deleted successfully.")
        return super().delete(request, *args, **kwargs)
