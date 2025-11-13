from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    skills = models.TextField()
    
    def __str__(self):
        return self.first_name
    
    
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    developers = models.ManyToManyField(Developer)
    
    def __str__(self):
        return self.title
    
    
    