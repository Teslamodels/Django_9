from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Sigma(TemplateView):
    template_name = 'index.html'

class Male(TemplateView):
    template_name = 'file.html'