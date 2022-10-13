from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='projects'),
    path('project_new/', views.project_new, name='project_new'),
]
