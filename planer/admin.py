from django.contrib import admin
from django.apps import apps
from . import models


# Register your models here.
my_models = apps.get_app_config('planer').get_models()
admin.site.register(my_models)
