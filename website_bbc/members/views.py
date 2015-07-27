from django.shortcuts import render
from django.http import HttpResponse

from members.models import ScientificSocietyMember, PharmaMember, PatientAssocMember

def index(request):
    context_dict = {}
    return render(request, 'members/index.html', context_dict)

def scientific_societies(request):
    members_list = ScientificSocietyMember.objects.order_by('-society')
    context_dic = {'members' : members_list, 'title' : 'Scientific Societies'}
    return render(request, 'members/index.html', context_dic)

def patient_associations(request):
    members_list = PatientAssocMember.objects.order_by('-society')
    context_dic = {'members' : members_list, 'title' : 'Patient Associations'}
    return render(request, 'members/index.html', context_dic)

def pharma_companies(request):
    members_list = PharmaMember.objects.order_by('-society')
    context_dic = {'members' : members_list, 'title' : 'Pharmaceutical Companies'}
    return render(request, 'members/index.html', context_dic)
