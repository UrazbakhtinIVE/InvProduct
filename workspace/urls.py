from django.urls import path
from django.contrib.auth.decorators import login_required
from workspace.views import *

urlpatterns = [
    path('', login_required(WorkSpaceView.as_view()), name='workspace'),
]