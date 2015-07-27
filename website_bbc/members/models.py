from django.db import models

class Member(models.Model):
    society = models.CharField(max_length=200, unique=True)
    address = models.TextField(max_length=200, blank=True)
    registration_number = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gsm = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    
    # Point of contact in the association
    name_contact = models.TextField(max_length=100, blank=True)
    title_contact = models.TextField(max_length=100, blank=True)
    address_contact = models.TextField(max_length=200, blank=True)
    phone_contact = models.CharField(max_length=20, blank=True)
    gsm_contact = models.CharField(max_length=20, blank=True)
    fax_contact = models.CharField(max_length=20, blank=True)
    website_contact = models.URLField(blank=True)
    email_contact = models.EmailField(blank=True)

    def __str__(self):
        return self.society

class PharmaMember(Member):
    pass
    
class ScientificSocietyMember(Member):
    pass

class PatientAssocMember(Member):
    pass


    
