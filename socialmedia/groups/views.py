from django.shortcuts import render

# Create your views here.

# views.py of groups app

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.core.urlresolvers import reverse

from . import Group, GroupMember

from django.views import generic

class CreateGroup(generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group