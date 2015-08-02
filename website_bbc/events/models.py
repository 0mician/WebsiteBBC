from django.db import models
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField

class SetOfFiles(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False,
                            help_text="Give a meaningful name to the set of file, for example 'BBCongress2015' (max 225 characters)")

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = "Set of files"

class File(models.Model):
    set = models.ForeignKey(SetOfFiles, verbose_name="Related Files")
    file = models.FileField()
    name = models.CharField(max_length=255, 
                            help_text="Give a meaningful name to the file, this name will be displayed on the webpage (max 255 characters)")

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

    name = models.CharField(max_length=255, 
                            help_text="Give a meaningful name to the event, for example 'Belgian Brain Congress 2015' (max 255 characters)")
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=3, choices=TYPE_OF_EVENT)
    url = models.URLField(null=True, blank=True,
                          help_text="optional, could be a link to the website of the event")
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=500, help_text="Give a short description of the event, it will be displayed on the homepage under events (max 500 characters)")
    details = HTMLField(null=True, 
                        help_text="This is for the event page, you can use style here, and are free to add as much content as you like")
    uploaded_files = models.ForeignKey(SetOfFiles, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
