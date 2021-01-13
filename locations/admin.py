from django.contrib import admin
from locations.models import Room, Titul


@admin.register(Titul)
class TitulAdmin(admin.ModelAdmin):
    list_display = ['number','name']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['titul','number','floor']
