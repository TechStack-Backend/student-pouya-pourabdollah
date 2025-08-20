from django.contrib import admin
from django.urls import path, include
from .views import developers, developer

app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', developers, name='developers'),
    path('/<str:username>', developer, name='developer')

]