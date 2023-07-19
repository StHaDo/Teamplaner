from django.shortcuts import render, redirect
from .forms import ProjectForm

from . import models


def home(request):

    context = {}

    return render(request, 'planer/index.html', context)


# Projects
def project_list(request):
    projects = models.Project.projects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'planer/project/project_list.html', context)


def project_detail(request, pk):
    project = models.Project.projects.get(pk=pk)

    context = {
        'project': project,
    }

    return render(request, 'planer/project/project_detail.html', context)


def project_new(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            if project.end != None:
                project.duration = project.end - project.start
                project.save()
            project.save()
            return redirect('project_detail', pk=project.id)

    context = {
        'form': form,
        'title': 'New Project',
        'headline': 'Create new Project',
    }

    return render(request, 'planer/project/project_new.html', context)


def project_update(request, pk):
    project = models.Project.projects.get(pk=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            if project.end != None:
                project.duration = project.end - project.start
                project.save()
            project.save()
            return redirect('projects')

    context = {
        'form': form,
        'title': 'Update Project',
        'headline': 'Update Project'
    }

    return render(request, 'planer/project/project_new.html', context)


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
