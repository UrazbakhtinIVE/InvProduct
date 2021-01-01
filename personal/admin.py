from django.contrib import admin
from personal.models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['firstName']


