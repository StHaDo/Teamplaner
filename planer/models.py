from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(verbose_name='Projektname', max_length=200)
    description = models.TextField(verbose_name='Projektbeschreibung')
    created_on = models.DateField(auto_now_add=True)
    start = models.DateField(
        verbose_name='Projektstart', blank=True, null=True)
    end = models.DateField(verbose_name='Projektende', blank=True, null=True)
    duration = models.DurationField(
        verbose_name='Projektdauer', blank=True, null=True)

    projects = models.Manager()

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS = [
        ('I', 'inactive'),
        ('A', 'active'),
        ('D', 'done'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='I')
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    tasks = models.Manager()

    def __str__(self):
        return self.name

    def set_date_if_completed(self):

        if self.completed and self.end == None:
            date_completed: date = date.today()
            return date_completed


class Comments(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    comments = models.Manager()

    def __str__(self) -> str:
        return (f'{self.user.username} - {self.task.name}')
