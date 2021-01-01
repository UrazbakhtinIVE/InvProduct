from django.contrib import admin
from mainapp.models import *
from printers.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PrinterSchedule)
class PrinterScheduleAdmin(admin.ModelAdmin):
    list_display = ['apper', 'printer',]





