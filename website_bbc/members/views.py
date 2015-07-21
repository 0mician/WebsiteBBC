from django.shortcuts import render
from django.http import HttpResponse

from members.models import ScientificSocietyMember

def index(request):
    context_dict = {}
    return render(request, 'members/index.html', context_dict)

def scientific_societies(request):
    members_list = ScientificSocietyMember.objects.order_by('-society')
    context_dic = {'scientific_societies' : members_list}
    return render(request, 'members/scientific_societies.html', context_dic)
