from django import forms
from django.contrib import admin
from printers.models import *


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']




@admin.register(PrinterStatus)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['name']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PrinterChoiceField(Category.objects.filter(slug='printers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PrinterChoiceField(forms.ModelChoiceField):
    pass



@admin.register(PrinterApplication)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['number']


@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PrinterAct)
class PrinterActModelAdmin(admin.ModelAdmin):
    list_display = ['number']




