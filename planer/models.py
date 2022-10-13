from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

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

    def __str__(self):
        return self.name

    def set_date_if_completed(completed: bool):

        if completed:
            date_completed: date = date.today()

        return date_completed


class Comments(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
