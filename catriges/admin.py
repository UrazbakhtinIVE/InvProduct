from django import forms
from django.contrib import admin
from catriges.models import *


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CartridgeModel)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CatrigeStatus)
class CatrigeStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Cartridge)
class CatrigeAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'CartridgeModel', 'original']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PrinterChoiceField(Category.objects.filter(slug='catriges'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PrinterChoiceField(forms.ModelChoiceField):
    pass


@admin.register(CartridgeApplication)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['number']


@admin.register(CartridgeAct)
class CartridgeActAdmin(admin.ModelAdmin):
    list_display = ['number']


