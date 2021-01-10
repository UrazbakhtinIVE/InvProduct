from django.views.generic import *
from .models import PrinterModel
from .forms import *
from django.urls import reverse_lazy

class PrintView(TemplateView):
    template_name = 'print/print.html'


class PrinterInfoView(TemplateView):
    template_name = 'print/printer_info.html'


class PrinterListView(ListView):
    model = Printer
    template_name = 'print/printer_list.html'
    context_object_name = 'printer'


class PrinterCreateView(CreateView):
    model = Printer
    template_name = 'print/printer_create_form.html'
    form_class = PrinterCreateForm
    context_object_name = 'pcf'


class PrinterModelListView(ListView):
    model = PrinterModel
    template_name = 'print/printer_models_list.html'
    queryset = PrinterModel.objects.all()
    context_object_name = 'pml'


class CreatePrinterModelView(CreateView):
    model = PrinterModel
    form_class = PrinterModelCreateForm
    template_name = 'print/printer_create_model.html'
    context_object_name = 'cpm'


class PrinterModelDetileView(DetailView):
    model = PrinterModel
    template_name = 'print/printer_model_detile.html'
    context_object_name = 'pmd'


class PrinterModelDeleteView(DeleteView):
    models = PrinterModel
    queryset = PrinterModel.objects.all()
    template_name = 'print/printer_model_delete.html'
    context_object_name = 'pmd'
    success_url = reverse_lazy('printer_model_list')


class PrinterUpdateView(UpdateView):
    model = PrinterModel
    template_name = 'print/printer_model_update.html'
    form_class = PrinterModelUpdateForm
    context_object_name = 'pmu'
    success_url = reverse_lazy('printer_model_list')






class PrinterScheduleView(ListView):
    model = PrinterSchedule
    template_name = 'print/printer_schedule_list.html'
    context_object_name = 'psl'


class CartridgeInfoView(TemplateView):
    pass
