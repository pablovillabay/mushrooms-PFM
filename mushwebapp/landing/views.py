import imp
from django.shortcuts import render
from django.views.generic import TemplateView

class Landing(TemplateView):
    template_name = 'landing_page.html'