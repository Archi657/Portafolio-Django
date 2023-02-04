from django.shortcuts import render
from .models import Projects, Profiles, Skills
import requests

def home(request):
    projects = Projects.objects.all()
    profiles = Profiles.objects.all()
    skills = Skills.objects.all()

    return render(request, 'home.html', {'projects' : projects,'profiles' : profiles,'skills' : skills  })
