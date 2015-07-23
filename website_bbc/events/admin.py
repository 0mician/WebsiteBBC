from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'location', 'uploaded_files']

admin.site.register(Event, EventAdmin)
