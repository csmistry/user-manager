from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Member



#Generic List view that displays members
#Corresponding template is in api/templates/api/member_list.html
class MembersList(ListView):
    model = Member

    #Overrides the default object_list name
    context_object_name = 'members'

   



#Generic detail view to edit member info
class MemberDetail(DetailView):
    model = Member
    context_object_name = 'member'
    template_name = 'api/member.html'