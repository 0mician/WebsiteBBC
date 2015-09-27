from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event
from news.models import News

def homepage(request):
    context_dict = {}
    events = Event.objects.order_by('-start')[:5]
    context_dict['events'] = events
    news = News.objects.order_by('-date')[:10]
    context_dict['news'] = news
    return render(request, 'home/index.html', context_dict)

def about(request):
    return render(request, 'home/about.html', {})

def about_fr(request):
    return render(request, 'home/about_fr.html', {})

def about_nl(request):
    return render(request, 'home/about_nl.html', {})

def about_en(request):
    return render(request, 'home/about_en.html', {})
