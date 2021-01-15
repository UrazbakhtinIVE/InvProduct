from django.shortcuts import render
from print.models import *
from django.views.generic import *




class ApplicationsView(TemplateView):
    template_name = 'cart/applications.html'


# class PrinterScheduleAppViewList(ListView):
#     model = PrinterSchedule
#     queryset = PrinterSchedule.objects.filter(status__name='На ремонт')
#     context_object_name = 'printer_shedule_list_app'
#     template_name='cart/printer_list_for_app.html'


class PrinterAppViewList(ListView):
    model = PrinterApp
    queryset = PrinterApp.objects.all()
    context_object_name = 'printer_app'
    template_name='cart/printer_list_for_app.html'



class PrinterSheduleAppViewDetile(DetailView):
    model = PrinterSchedule
    queryset = PrinterSchedule.objects.all()
    context_object_name = 'printer_shedule_detile'
    template_name = 'cart/printer_detile_for_app.html'



# class PrinterAppListView(ListView):
#     model = PrinterApp
#     queryset = PrinterApp.objects.all()
#     context_object_name = 'printer_app_list'
#     template_name = 'cart/app_list'




class PrinterSheduleUpdateStatusAppView(UpdateView):
    model = PrinterSchedule
    quryser = PrinterSchedule.objects.filter(status__name='На ремонт')
    context_object_name = 'psus'
    template_name = 'cart/printer_status_update.html'





