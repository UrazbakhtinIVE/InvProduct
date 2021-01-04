from django.contrib import admin

from workspace.models import *


@admin.register(MonitorModel)
class MonitorModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class MonitorChoiceField(object):
    pass


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','model', 'status']

  
@admin.register(StatusWork)
class StatusWorkAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PCModel)
class PCModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = ['name', 'serialNumber','status']

@admin.register(TokenModel)
class TokenModelAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','tokenModel']


@admin.register(TelephoneModel)
class  TelephoneModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','modelTelephone']



@admin.register(PowerModel)
class  PowerModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','powerModel']



@admin.register(ActWorkSpace)
class ActWorkSpaceAdmin(admin.ModelAdmin):
    list_display = ['number', 'person', 'date']

@admin.register(WorkSpaceSchedule)
class WorkSpaceScheduleAdmin(admin.ModelAdmin):
    list_display = ['apper','date']


