from django.urls import path
from django.contrib.auth.decorators import login_required
from mainapp.views import *

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('print/', login_required(PrintView.as_view()), name='print')
]