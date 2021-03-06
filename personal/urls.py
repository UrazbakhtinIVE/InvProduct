from django.urls import path
from django.contrib.auth.decorators import login_required
from personal.views import *




urlpatterns = [
    path('', login_required(PersonView.as_view()), name='person'),
    path('list/', login_required(PersonListView.as_view()), name='list_person'),
    path('phone/', PersonalTelephoneListView.as_view(), name='phone_person'),
]