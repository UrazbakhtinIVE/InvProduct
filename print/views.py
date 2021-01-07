from django.views.generic import *
from .models import *

class PrintView(TemplateView):
    template_name = 'print/print.html'

class PrinterInfoView(TemplateView):
    template_name = 'print/printer_info.html'




class PrinterListView(ListView):
    model = Printer
    template_name = 'print/printerList.html'
    context_object_name = 'printer'


class CartrigeInfoView(TemplateView):
    template_name = ''
