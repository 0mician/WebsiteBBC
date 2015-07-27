from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event, File

def index(request):
    events_list = Event.objects.order_by('-start')
    files_list = File.objects.get(uploaded_files=uploaded_files)
    context_dict = {'events_list' : events_list}    
    return render(request, 'events/index.html', context_dict)
