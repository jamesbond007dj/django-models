from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Gibson

class HomePageView(ListView):
    template_name = 'home.html'
    model = Gibson
    context_object_name = 'gibson'

class GibsonDetailView(DetailView):
    template_name = 'gibson_detail.html'
    model = Gibson
    context_object_name = 'gibson'