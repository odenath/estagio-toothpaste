from django.contrib import admin

from . import models

# Register your models here.

admin.register(models.User)
admin.register(models.Person)
admin.register(models.Dentist)
