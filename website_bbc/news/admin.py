from django.contrib import admin

from news.models import News
from events.models import File, SetOfFiles

class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    fieldsets = (
        (None, {
            'fields' : ('name', 'date', 'url', 'description', 'details', 'uploaded_files')
            }),
        )

admin.site.register(News, NewsAdmin)
