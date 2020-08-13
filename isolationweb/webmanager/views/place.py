from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from webmanager.models import Place, Person, ConnectedPlace


class EditPlaceView(generic.DetailView):
    model = Place
    template_name = 'place.html'

def edit_place(request):
    a = 1 + 1
