from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='news_home'),
    url(r'(?P<news_slug>[\w\-]+)/$', views.news_details, name='news_detail'),
]
