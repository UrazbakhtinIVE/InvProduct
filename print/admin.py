from django.contrib import admin
from print.models import *


@admin.register(PrinterStatus)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CartridgeStatus)
class CartridgeStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Type)
class PrinterTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Color)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CartridgeModel)
class CartridgeModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['serialNumber']


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PrinterSchedule)
class PrinterScheduleAdmin(admin.ModelAdmin):
    list_display = ['apper']



@admin.register(PrinterAct)
class PrinterActAdmin(admin.ModelAdmin):
    list_display = ['number']



@admin.register(PrinterApp)
class PrinterActAdmin(admin.ModelAdmin):
    list_display = ['id']

