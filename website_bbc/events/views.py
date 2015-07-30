from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event, File

def index(request):
    events_list = Event.objects.order_by('-start')
    context_dict = {'events_list' : events_list}    
    return render(request, 'events/index.html', context_dict)

def event_details(request, event_slug):
    context_dict = {}
    print(event_slug)
    try:
        event = Event.objects.get(slug=event_slug)
        context_dict['event'] = event
        files = File.objects.filter(set=event.uploaded_files)
        context_dict['files'] = files
    except Event.DoesNotExist:
        pass

    return render(request, 'events/details.html', context_dict)
