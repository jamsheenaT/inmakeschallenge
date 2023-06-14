from django.db import models
from pyexpat import model


# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image')
    desc=models.TextField()

    def __str__ (self):
          return self.name

class team(models.Model):
    teamname=models.CharField(max_length=250)
    teamimage=models.ImageField(upload_to='teamimage')
    description=models.TextField()

    def __str__(self):
       return  self.teamname

