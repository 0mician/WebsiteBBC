from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'about/$', views.about, name='about'),
    url(r'about/fr/$', views.about_fr, name='about_fr'),
    url(r'about/nl/$', views.about_nl, name='about_nl'),
    url(r'about/en/$', views.about_en, name='about_en'),
]
