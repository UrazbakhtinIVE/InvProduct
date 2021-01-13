from django.urls import path
from django.contrib.auth.decorators import login_required
from workspace.views import *

urlpatterns = [
    path('', login_required(WorkSpaceView.as_view()), name='workspace'),
    path('equipment/', login_required(EquipmentView.as_view()), name='equipment'),
    path('equipment/pc/', login_required(PCView.as_view()), name='pc'),
    path('equipment/pc/list/', login_required(PCListView.as_view()), name='pc_list'),
    path('equipment/pc/model/', login_required(PCModelView.as_view()), name='pc_model'),
    path('equipment/acts/', login_required(ActView.as_view()), name='acts'),
    path('equipment/acts/list/', login_required(ActListView.as_view()), name='acts_list'),
    path('list/', WorkSpaceListView.as_view(), name='wc_list'),
]