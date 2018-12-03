from django.contrib import admin

from .models import Event
from .models import Teetime


class EventList(admin.ModelAdmin):
    list_display = ('event_name', 'organization', 'contact_number' )
    list_filter = 'organization'
    search_fields = 'organization'
    ordering = ['event_name']


admin.site.register(Event)


class TeeTimeList(admin.ModelAdmin):
    list_display = ('Teetime_Name', 'Teetime_Start', 'Golfers_Attending')
    list_filter = 'Teetime_start'
    search_fields = 'Teetime_Start'
    ordering = ['Teetime_Start']


admin.site.register(Teetime)