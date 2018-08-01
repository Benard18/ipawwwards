from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project


@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {"projects": projects})


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {"user": user})