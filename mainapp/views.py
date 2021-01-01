from django.views.generic import *


class HomeView(TemplateView):
    template_name = 'mainapp/index.html'


class PrintView(TemplateView):
    template_name = 'mainapp/print.html'
