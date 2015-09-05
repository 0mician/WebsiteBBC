from django.db import models

from tinymce.models import HTMLField
from events.models import SetOfFiles, File 

class News(models.Model):
    name = models.CharField(max_length=255, 
                            help_text="Give a meaningful name to the news (max 255 characters)")
    slug = models.SlugField(unique=True)
    url = models.URLField(null=True, blank=True,
                          help_text="optional, could be a link to a website, more URL can be added in the details section")
    date = models.DateField()
    description = models.CharField(max_length=500, help_text="Give a short description of the event, it will be displayed on the homepage under events (max 500 characters)")
    details = HTMLField(null=True, 
                        help_text="This is for the news details page, you can use style here, and are free to add as much content as you like")
    uploaded_files = models.ForeignKey(SetOfFiles, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
