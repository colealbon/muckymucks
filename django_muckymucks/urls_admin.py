from django.conf.urls.defaults import *
from django.contrib import admin
from django.db.models import get_app, get_models
admin.autodiscover()

urlpatterns = patterns ('',
    (r'^(.*)', admin.site.root),
)
