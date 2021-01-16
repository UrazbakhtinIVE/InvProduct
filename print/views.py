from django.views.generic import *
from .models import PrinterModel
from .forms import *
from django.urls import reverse_lazy


class PrintView(TemplateView):
    template_name = 'print/print.html'


class PrinterInfoView(ListView):
    model = Printer
    template_name = 'print/printer_info.html'
    context_object_name = 'printer'


class PrinterListView(ListView):
    model = Printer
    template_name = 'print/printer_list.html'
    context_object_name = 'printer'


class PrinterDetileView(DetailView):
    model = Printer
    template_name = 'print/printer_detile.html'
    context_object_name = 'printer'


class PrinterCreateView(CreateView):
    model = Printer
    template_name = 'print/printer_create.html'
    form_class = PrinterCreateForm
    context_object_name = 'pcf'


class PrinterDeleteView(DeleteView):
    model = Printer
    template_name = 'print/printer_delete.html'
    context_object_name = 'pd'
    success_url = reverse_lazy('printer_list')


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
    model = Printer
    template_name = 'print/printer_update.html'
    form_class = PrinterUpdateForm
    context_object_name = 'pmu'
    success_url = reverse_lazy('printer_list')




class PrinterUpdateStatusView(UpdateView):
    model = Printer
    template_name = 'print/printer_status_update.html'
    form_class = PrinterUpdateStatusForm
    context_object_name = 'pmus'
    success_url = reverse_lazy('printer_list')





class PrinterModelUpdateView(UpdateView):
    model = PrinterModel
    template_name = 'print/printer_model_update.html'
    form_class = PrinterModelUpdateForm
    context_object_name = 'pmu'
    success_url = reverse_lazy('printer_model_list')





class PrinterScheduleListView(ListView):
    model = PrinterSchedule
    template_name = 'print/printer_schedule_list.html'
    context_object_name = 'psl'

class PrinterSheduleDetileView(DetailView):
    model = PrinterSchedule
    template_name = 'print/printer_shedule_detile.html'
    context_object_name = 'psd'


class PrinterScheduleCreateView(CreateView):
    model =  PrinterSchedule
    template_name = 'print/printer_create_shedule.html'
    form_class =PrinterScheduleCreateForm
    success_url = reverse_lazy('printer_schedule')






class CartridgeInfoView(TemplateView):
    pass






