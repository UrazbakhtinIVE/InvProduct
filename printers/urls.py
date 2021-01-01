from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from printers.views import *

urlpatterns = [
    path('', login_required(PrinterView.as_view()), name='printer'),


    # path('list/', login_required(PrinterListView.as_view()), name='printerList'),
    # path('detile/<int:pk>/', login_required(PrinterDetileView.as_view()), name='printer_detail'),
    # path('create/', login_required(PrinterCreateView.as_view()), name='printer_create'),
    # path('update/<int:pk>/', login_required(PrinterUpdateView.as_view()), name='printer_update'),
    #
    # path('prtinter/schedul/list/', login_required(PrinterScheduleList.as_view()), name = 'printerScheduleList'),
    # path('prtinter/schedul/detile/<int:pk>/', login_required(PrinterScheduleDetileView.as_view()), name='printerSchedule_detail'),
    # path('compatibility/',login_required(PrinterCatrigeList.as_view()), name='compatibility'),
    # path('compatibility/<int:pk>/', login_required(PrinterCatrigeDetile.as_view()), name ='compatibility_detile'),
    # path('schedule/create/', login_required(PrinterSchedulePrinterCreate.as_view()), name='printerSchedulePrinterCreate'),
    # path('schedule/repairsList/', login_required(PrinterRepairsList.as_view()), name='repairsList'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)