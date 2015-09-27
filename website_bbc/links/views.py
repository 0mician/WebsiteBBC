from django.shortcuts import render

from links.models import Link

def index(request):
    links_list = Link.objects.order_by('name')
    context_dict = {'links_list' : links_list}
    return render(request, 'links/index.html', context_dict)

