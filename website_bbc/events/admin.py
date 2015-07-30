from django.contrib import admin
from events.models import Event, File, SetOfFiles

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'category', 'uploaded_files']
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'url', 'start', 'end', 'details', 'uploaded_files')
        }),
    )

class FileInline(admin.TabularInline):
    model = File

class SetOfFilesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [FileInline]

admin.site.register(SetOfFiles, SetOfFilesAdmin)
admin.site.register(Event, EventAdmin)
