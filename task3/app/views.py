from django.shortcuts import render, redirect
from .models import Developer, Project, Skill
from .forms import DeveloperForm, ProjectForm


def home(request):
    developers = Developer.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {'developers': developers, 'projects':projects})  

def developer(request):
    developers = Developer.objects.all()
    return render(request, 'developers.html', {'developers': developers})    

def developer_detail(request, pk):
    developer = Developer.objects.get(id = pk)
    detail = {
        'first_name': developer.first_name,
        'last_name': developer.last_name,
        'email': developer.email,
        'age': developer.age,
        'projects': list(Project.objects.filter(developer = developer)),
        'skills': list(Skill.objects.filter(developer = developer))
    }
    return render(request, 'developer_detail.html', {'detail': detail})


def add_developer(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')
    else:
        form = DeveloperForm()
    return render(request, 'add_developer.html', {'form': form})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(id = pk)
    detail = {
        'title': project.title,
        'description': project.description,
        'developers': list(Developer.objects.filter(project = project))
    }
    return render(request, 'project_detail.html', {'detail': detail})
