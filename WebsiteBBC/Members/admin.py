from django.contrib import admin

from Members.models import Member, Representative

admin.site.register(Member)
admin.site.register(Representative)
