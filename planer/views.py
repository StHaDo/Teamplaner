from django.shortcuts import render, redirect
from .forms import ProjectForm

from . import models


def home(request):

    context = {}

    return render(request, 'planer/index.html', context)


# Projects
def project_list(request):
    projects = models.Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'planer/project/project_list.html', context)


def project_detail(request, pk):
    pass


def project_new(request):
    form = ProjectForm()

    context = {
        'form': form,
    }

    return render(request, 'planer/project/project_new.html', context)


def project_update(request, pk):
    pass


def project_delete(request, pk):
    pass


# Tasks

def task_list(request):
    pass


def task_new(request):
    pass


def task_update(request):
    pass


def task_delete(request):
    pass


# Comments
def comment_new(request):
    pass
