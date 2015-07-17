from django.contrib import admin

from members.models import (
    PharmaMember, 
    PatientAssocMember, 
    ScientificSocietyMember)


class MemberAdmin(admin.ModelAdmin):
    list_display = ['society', 'website', 'name_contact', 'title_contact']
    fieldsets = (
        ('Society Information', {
            'fields' : ('society', 'address', 'registration_number', 'phone',
                        'gsm', 'fax', 'website', 'email')}),
        ('Contact Information', {
            'fields' : ('name_contact', 'title_contact', 'address_contact', 
                        'phone_contact', 'gsm_contact', 'fax_contact', 'website_contact', 
                        'email_contact')})
    )
    

admin.site.register(PharmaMember, MemberAdmin)
admin.site.register(PatientAssocMember, MemberAdmin)
admin.site.register(ScientificSocietyMember, MemberAdmin)

