from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView

from django_datacite.views import resource, resource_json, resource_xml


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(pattern_name='admin:index')),
    re_path(r'^(?P<identifier>\d{2}\.\d+\/[A-Za-z0-9_.\-\/]+).xml$', resource_xml, name='resource_xml'),
    re_path(r'^(?P<identifier>\d{2}\.\d+\/[A-Za-z0-9_.\-\/]+).json$', resource_json, name='resource_json'),
    re_path(r'^(?P<identifier>\d{2}\.\d+\/[A-Za-z0-9_.\-\/]+)', resource, name='resource')
]
