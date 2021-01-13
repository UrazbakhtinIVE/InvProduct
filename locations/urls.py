from django.contrib.auth.decorators import login_required
from django.urls import path
from locations.views import *

urlpatterns = [
    path('', login_required(locationView.as_view()), name='loc'),
]
