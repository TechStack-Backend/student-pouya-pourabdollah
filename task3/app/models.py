from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.first_name +' '+ self.last_name
    
class Project(models.Model):
    developer = models.ManyToManyField(Developer)
    title = models.CharField(max_length=50)
    description = models.TextField()
    
class Skill(models.Model):
    developer = models.ForeignKey(Developer, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    

