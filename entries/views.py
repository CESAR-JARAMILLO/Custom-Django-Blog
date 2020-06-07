from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView
# Create your views here.

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'entries'
