from django.views.generic import *
from locations.models import *

class locationView(ListView):
    model = Room
    queryset = Room.objects.all()
    template_name = 'location/location.html'
    context_object_name = 'loc'
