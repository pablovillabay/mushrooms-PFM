import imp
from django.shortcuts import render
from django.views.generic import TemplateView

class Dataclass(TemplateView):
    template_name = 'dataclass_page.html'