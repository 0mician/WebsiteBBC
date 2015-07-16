from django.db import models

class Member(models.Model):
    TYPE_OF_MEMBER = (
        ('PH', 'Pharmaceutical Company'),
        ('PA', 'Patient Association'),
        ('SC', 'Scientific Society'),
    )

    society = models.CharField(max_length=250, unique=True)
    category = models.CharField(max_length=2, choices=TYPE_OF_MEMBER)
    address = models.TextField(max_length=400)
    phone = models.CharField(max_length=20)
    gsm = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    website = models.URLField()
    email = models.EmailField()

class Representative(models.Model):
    society = models.ForeignKey('Member')
    name = models.TextField(max_length=200)
    title = models.TextField(max_length=400)
    address = models.TextField(max_length=400)
    phone = models.CharField(max_length=20)
    gsm = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    website = models.URLField()
    email = models.EmailField()
