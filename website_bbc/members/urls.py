from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'scientific_societies/$', views.scientific_societies, name='scientific_society'),
    url(r'pharmaceutical_companies/$', views.pharma_companies, name='pharmaceutical_companies'),
    url(r'patient_associations/$', views.patient_associations, name='patient_associations'),
]
