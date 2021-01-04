from django.views.generic import *

from workspace.models import *


class WorkSpaceView(TemplateView):
    template_name = 'workspace/workspace.html'


class EquipmentView(TemplateView):
    template_name = 'workspace/equipment.html'


class PCView(TemplateView):
    template_name = 'workspace/pc.html'


class ActView(TemplateView):
    template_name = 'workspace/act_workspace.html'

class ActListView(ListView):
    template_name = 'workspace/act_list.html'
    queryset = ActWorkSpace.objects.all()
    context_object_name = 'act'


class PCListView(ListView):
    template_name = 'workspace/pc_list.html'
    queryset = PC.objects.all()
    context_object_name = 'pc'


class PCModelView(ListView):
    template_name = 'workspace/pc_model_list.html'
    queryset = PCModel.objects.all()
    context_object_name = 'pcModel'




class WorkSpaceListView(ListView):
    template_name = 'workspace/list_workspace.html'
    queryset =  PC.objects.all()
    context_object_name = 'ws'