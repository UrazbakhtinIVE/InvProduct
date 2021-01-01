from django.views.generic import TemplateView


class PrinterView(TemplateView):
    template_name = 'printers/printer_info.html'


