from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm
from django.contrib import messages


class DeveloperView(View):
    template_list = 'developer_list.html'
    template_detail = 'developer_detail.html'
    template_form = 'developer_form.html'
    template_confirm = 'developer_confirm_delete.html'

    def get(self, request, pk=None):
        if pk:
            if 'delete' in request.path:
                developer = get_object_or_404(Developer, pk=pk)
                return render(request, self.template_confirm, {'developer': developer})
            
            if 'update' in request.path:
                return self.get_form(request, pk=pk)
            
            developer = get_object_or_404(Developer, pk=pk)
            return render(request, self.template_detail, {'developer': developer})
        else:
            if 'create' in request.path:
                return self.get_form(request)
            
            developers = Developer.objects.all()
            return render(request, self.template_list, {'developers': developers})

    def post(self, request, pk=None):
        if 'delete' in request.path and pk:
            developer = get_object_or_404(Developer, pk=pk)
            try:
                messages.success(request, "Developer deleted successfully!")
                developer.delete()
                return HttpResponseRedirect(reverse('developer-list'))
            except Exception as e:
                return render(request, self.template_confirm, {'developer': developer, 'error': str(e)})

        if pk:
            developer = get_object_or_404(Developer, pk=pk)
            form = DeveloperForm(request.POST, instance=developer)
        else:
            form = DeveloperForm(request.POST)

        try:
            if form.is_valid():
                messages.success(request, "Developer saved successfully!")
                form.save()
                return HttpResponseRedirect(reverse('developer-list'))
        except Exception as e:
            return render(request, self.template_form, {'form': form, 'error': str(e)})

        return render(request, self.template_form, {'form': form})


    def get_form(self, request, pk=None):
        if pk:
            developer = get_object_or_404(Developer, pk=pk)
            form = DeveloperForm(instance=developer)
        else:
            form = DeveloperForm()
        return render(request, self.template_form, {'form': form})



class ProjectView(View):
    template_list = 'project_list.html'
    template_detail = 'project_detail.html'
    template_form = 'project_form.html'
    template_confirm = 'project_confirm_delete.html'

    def get(self, request, pk=None):
        if pk:
            if 'delete' in request.path:
                project = get_object_or_404(Project, pk=pk)
                return render(request, self.template_confirm, {'project': project})
            
            if 'update' in request.path:
                return self.get_form(request, pk=pk)
            
            project = get_object_or_404(Project, pk=pk)
            return render(request, self.template_detail, {'project': project})
        else:
            if 'create' in request.path:
                return self.get_form(request)
            
            projects = Project.objects.all()
            return render(request, self.template_list, {'projects': projects})

    def post(self, request, pk=None):
        if 'delete' in request.path and pk:
            project = get_object_or_404(Project, pk=pk)
            try:
                messages.success(request, "Project deleted successfully!")
                project.delete()
                return HttpResponseRedirect(reverse('project-list'))
            except Exception as e:
                return render(request, self.template_confirm, {'project': project, 'error': str(e)})

        if pk:
            project = get_object_or_404(Project, pk=pk)
            form = ProjectForm(request.POST, instance=project)
        else:
            form = ProjectForm(request.POST)

        try:
            if form.is_valid():
                messages.success(request, "Project saved successfully!")
                form.save()
                return HttpResponseRedirect(reverse('project-list'))
        except Exception as e:
            return render(request, self.template_form, {'form': form, 'error': str(e)})

        return render(request, self.template_form, {'form': form})


    def get_form(self, request, pk=None):
        if pk:
            project = get_object_or_404(Project, pk=pk)
            form = ProjectForm(instance=project)
        else:
            form = ProjectForm()
        return render(request, self.template_form, {'form': form})
