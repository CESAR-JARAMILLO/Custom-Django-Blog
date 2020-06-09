from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'entries'

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['title', 'text']
