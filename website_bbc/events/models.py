from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(max_length=10000, blank=True)
    uploaded_files = models.FileField(null=True)
