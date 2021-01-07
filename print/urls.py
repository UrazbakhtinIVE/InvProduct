from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(PrintView.as_view()), name='print'),
    path('printers/', login_required(PrinterInfoView.as_view()), name='printer_info'),
    path('printers/list/', login_required(PrinterListView.as_view()), name='printer_list'),
    path('cartridges/', login_required(CartrigeInfoView.as_view()), name='cartridge'),

]

