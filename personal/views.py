from django.views.generic import *

from personal.models import *


class PersonView(TemplateView):
    template_name = 'mainapp/persons.html'


class PersonListView(ListView):
    template_name = 'personal/personList.html'
    context_object_name = 'persons'
    queryset = Persons.objects.all()
