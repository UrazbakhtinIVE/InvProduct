from django.contrib import admin

from workspace.models import *


@admin.register(MonitorModel)
class MonitorModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class MonitorChoiceField(object):
    pass


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','model', 'status','loc']

  
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
    list_display = ['name', 'serialNumber','status', 'loc']

@admin.register(TokenModel)
class TokenModelAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','tokenModel']


@admin.register(ActWorkSpace)
class ActWorkSpaceAdmin(admin.ModelAdmin):
    list_display = ['number']




