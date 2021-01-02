from django.views.generic import *

from personal.models import *


class WorkSpaceView(TemplateView):
    template_name = 'workspace/workspace.html'


