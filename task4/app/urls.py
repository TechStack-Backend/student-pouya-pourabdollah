from django.urls import path
from .views import DeveloperView, ProjectView

urlpatterns = [

    path('developers/', DeveloperView.as_view(), name='developer-list'),
    path('developers/create/', DeveloperView.as_view(), name='developer-create'),
    path('developers/<int:pk>/', DeveloperView.as_view(), name='developer-detail'),
    path('developers/<int:pk>/update/', DeveloperView.as_view(), name='developer-update'),
    path('developers/<int:pk>/delete/', DeveloperView.as_view(), name='developer-delete'),

    path('projects/', ProjectView.as_view(), name='project-list'),
    path('projects/create/', ProjectView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectView.as_view(), name='project-delete'),
]