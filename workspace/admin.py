from django.contrib import admin

from workspace.models import *


@admin.register(MonitorModel)
class MonitorModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','model', 'status','loc']

@admin.register(StatusWork)
class StatusWorkAdmin(admin.ModelAdmin):
    list_display = ['name']
