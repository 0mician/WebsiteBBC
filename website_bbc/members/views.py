from django.shortcuts import render
from django.http import HttpResponse

from members.models import ScientificSocietyMember, PharmaMember, PatientAssocMember

def index(request):
    context_dict = {}
    return render(request, 'members/index.html', context_dict)

def scientific_societies(request):
    members_list = ScientificSocietyMember.objects.order_by('-society')
    context_dic = {'scientific_societies' : members_list}
    return render(request, 'members/scientific_societies.html', context_dic)

def patient_associations(request):
    members_list = PatientAssocMember.objects.order_by('-society')
    context_dic = {'patient_associations' : members_list}
    return render(request, 'members/patient_associations.html', context_dic)

def pharma_companies(request):
    members_list = PharmaMember.objects.order_by('-society')
    context_dic = {'pharmaceutical_companies' : members_list}
    return render(request, 'members/pharmaceutical_companies.html', context_dic)

