from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from .views import PrinterModelListView, PrinterCreateView, PrinterModelDetileView, PrinterModelDeleteView


urlpatterns = [
    path('', login_required(PrintView.as_view()), name='print'),
    path('printers/', login_required(PrinterInfoView.as_view()), name='printer_info'),
    path('printers/list/', login_required(PrinterListView.as_view()), name='printer_list'),
    path('create/', login_required(PrinterCreateView.as_view()), name='printer_create'),
    path('printers/model/list/', login_required(PrinterModelListView.as_view()), name='printer_model_list'),
    path('printers/model/detile/<int:pk>/', login_required(PrinterModelDetileView.as_view()), name='printer_model_detile'),
    path('printers/model/create/', login_required(CreatePrinterModelView.as_view()), name='printer_model_create'),
    path('printers/model/update/<int:pk>/', login_required(PrinterUpdateView.as_view()), name='printer_model_update'),
    path('printers/schedule/', login_required(PrinterScheduleView.as_view()), name='printer_schedule'),


    path('printers/delete/<int:pk>/', login_required(PrinterModelDeleteView.as_view()), name='printer_model_delete'),


    path('cartridges/', login_required(CartridgeInfoView.as_view()), name='cartridge'),

]
