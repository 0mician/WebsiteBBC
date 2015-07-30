from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='events_home'),
    url(r'(?P<event_slug>[\w\-]+)/$', views.event_details, name='event_detail'),
]
