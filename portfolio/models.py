from django.db import models
import datetime

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/static/project/')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

class Profil(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20,default="Software Engineer")
    images = models.ImageField(upload_to='portfolio/static/profile/')
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=30)
    bog = models.CharField(max_length=300)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.title