from django.contrib import admin
from django.urls import path, include
from .views import home, developer, developer_detail, add_developer, project_detail, add_project, projects

urlpatterns = [
    path('home', home, name='home'),
    path('developers', developer, name='developers'),
    path('developers/<int:pk>/', developer_detail, name='developer_detail'),
    path('add_developer', add_developer, name='add_developer'),
    path('projects<int:pk>', project_detail, name='project_detail'),
    path('add_project', add_project, name='add_project'),
    path('projects', projects, name='projects')
] 
