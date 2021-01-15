from .views import *
from .views import *
from django.contrib.auth.decorators import login_required
from django.urls import path
from print.models import *
from cart.models import *

urlpatterns = [
    path('', login_required(ApplicationsView.as_view()), name='applications'),
    # path('printerapp/list/', login_required(PrinterScheduleAppViewList.as_view()), name='app_printer_shedule'),
    path('printerapp/list/', login_required(PrinterAppViewList.as_view()), name='app_printer_shedule'),
    path('shedule/detile/<int:pk>/',PrinterSheduleAppViewDetile.as_view(), name='shedule_app_detile'),
    # path('printerapp/list/', login_required(PrinterAppListView.as_view()), name='app_printer_list'),


]
