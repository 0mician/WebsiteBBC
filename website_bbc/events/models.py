from django.db import models
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField

class SetOfFiles(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = "Set of files"

class File(models.Model):
    set = models.ForeignKey(SetOfFiles, verbose_name="Related Files")
    file = models.FileField()
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)

class Event(models.Model):

    TYPE_OF_EVENT = (
        ('BAW', 'Brain Awareness Week'),
        ('BBC', 'Belgian Brain Congress'),
        ('EBC', 'European Brain Council'),
        ('OTH', 'Other')
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=3, choices=TYPE_OF_EVENT)
    url = models.URLField(null=True, blank=True)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=500)
    details = HTMLField(null=True)
    uploaded_files = models.ForeignKey(SetOfFiles, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
