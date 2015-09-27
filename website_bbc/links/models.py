from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False,
                            help_text="Name of the association")
    url = models.URLField(help_text="link to the association's website")
    
    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return self.name
