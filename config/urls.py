from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_datacite.urls', namespace='datacite')),
    path('', RedirectView.as_view(pattern_name='admin:index')),
]
