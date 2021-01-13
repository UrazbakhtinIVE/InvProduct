from django.contrib import admin
from mainapp.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']








