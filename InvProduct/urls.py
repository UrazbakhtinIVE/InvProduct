from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from pip._vendor.html5lib.constants import namespaces

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('home/', include('mainapp.urls')),
    path('print/', include('print.urls')),
    path('persons/',include('personal.urls')),
    path('workspace/', include('workspace.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = '/'
