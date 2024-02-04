from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from .models import Project, Profil, Blog


# Create your views here.

def homepage(request):
    pro = Project.objects.all()
    prof = Profil.objects.all()
    blog = Blog.objects.all().filter().order_by('-date')

    print(prof)
    return render(request, 'homepage.html', {'Project': pro, 'Profile': prof, 'Blog': blog})



