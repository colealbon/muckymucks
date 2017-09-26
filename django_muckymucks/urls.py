from django.conf.urls.defaults import *
from django.contrib.databrowse import views
from django_muckymucks import views
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns ('',
    (r'^databrowse/', include('django_muckymucks.urls_databrowse')),
    (r'^admin/', include('django_muckymucks.urls_admin')),
    (r'^(.*)', admin.site.root),
)
