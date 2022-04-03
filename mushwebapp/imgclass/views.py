import imp
from django.shortcuts import render
from django.views.generic import TemplateView

class IMGclass(TemplateView):
    template_name = 'imgclass_page.html'