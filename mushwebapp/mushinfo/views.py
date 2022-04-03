import imp
from django.shortcuts import render
from django.views.generic import TemplateView

class Mushinfo(TemplateView):
    template_name = 'mushinfo_page.html'