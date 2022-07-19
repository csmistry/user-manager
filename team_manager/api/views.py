from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Member

#Generic List view that displays members
#Corresponding template is in api/templates/api/member_list.html
class MembersList(ListView):
    model = Member

    #Overrides the default object_list name
    context_object_name = 'members'

   

#add a new team member
class MemberCreate(CreateView):
    model = Member
    
    #show all fields of the Member class
    fields = '__all__'

    #after creating a member, redirect to members list
    success_url = reverse_lazy('members')
    template_name = 'api/member_create.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(MemberCreate, self).get_form(form_class)
        form.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'formTextEntry'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'formTextEntry'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'formTextEntry', 'required': True, 'placeholder': 'Email'})
        form.fields['phone'].widget = forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'formTextEntry'})
        form.fields['role'] = forms.ChoiceField(
            choices = Member.Role.choices,
            widget=forms.RadioSelect(),
            initial= Member.Role.REGULAR,
        )
        return form

#Edit team member info
class MemberEdit(UpdateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')
    template_name = 'api/member_edit.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(MemberEdit, self).get_form(form_class)
        form.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'formTextEntry'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'formTextEntry'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'formTextEntry', 'required': True, 'placeholder': 'Email'})
        form.fields['phone'].widget = forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'formTextEntry'})
        form.fields['role'] = forms.ChoiceField(
            choices = Member.Role.choices,
            widget=forms.RadioSelect(),
            initial= form.fields['role'],
        )
        
        return form

#delete team member
class MemberDelete(DeleteView):
    model = Member
    context_object_name = 'member'
    template_name = 'api/member_delete.html'
    success_url = reverse_lazy('members')
