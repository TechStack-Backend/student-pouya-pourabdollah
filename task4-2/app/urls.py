"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    DeveloperListView, DeveloperDetailView, DeveloperCreateView,
    DeveloperUpdateView, DeveloperDeleteView,
    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView,
)

urlpatterns = [
    path('developers/', DeveloperListView.as_view(), name='developer_list'),
    path('developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer_detail'),
    path('developers/create/', DeveloperCreateView.as_view(), name='developer_create'),
    path('developers/<int:pk>/update/', DeveloperUpdateView.as_view(), name='developer_update'),
    path('developers/<int:pk>/delete/', DeveloperDeleteView.as_view(), name='developer_delete'),

    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]

