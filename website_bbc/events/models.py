from django.db import models

class SetOfFiles(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)

    def __str__(self):
        return self.name 

class File(models.Model):
    set = models.ForeignKey(SetOfFiles, verbose_name="Related Files")
    file = models.FileField()
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)

class Event(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(max_length=10000, blank=True)
    uploaded_files = models.ForeignKey(SetOfFiles, null=True)
