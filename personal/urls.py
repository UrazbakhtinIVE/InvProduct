from django.urls import path
from django.contrib.auth.decorators import login_required
from personal.views import *


urlpatterns = [
    path('', login_required(PersonView.as_view()), name='person'),
    path('list/', login_required(PersonListView.as_view()), name='list_person'),
    path('servicePhoneList/', login_required(PostListView.as_view()), name='service_phone'),
]