from django.views.generic import *
from .models import *
from .forms import *


class PrintView(TemplateView):
    template_name = 'print/print.html'


class PrinterInfoView(TemplateView):
    template_name = 'print/printer_info.html'


class PrinterListView(ListView):
    model = Printer
    template_name = 'print/printerList.html'
    context_object_name = 'printer'


class PrinterCreateView(CreateView):
    model = Printer
    template_name = 'print/printerCreateForm.html'
    form_class = PrinterCreateForm
    context_object_name = 'pcf'


class PrinterModelListView(ListView):
    model = PrinterModel
    template_name = 'print/printerModelsList.html'
    queryset = PrinterModel.objects.all()
    context_object_name = 'pml'


class CreatePrinterModelView(CreateView):
    model = PrinterModel
    form_class = PrinterModelCreateForm
    template_name = 'print/printer_create_model.html'
    context_object_name = 'cpm'







class CartridgeInfoView(TemplateView):
    pass
