from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    context_dict = {}    
    return render(request, 'home/index.html', context_dict)

