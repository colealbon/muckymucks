from django.conf.urls.defaults import *
from django.contrib import databrowse
from django_muckymucks.muckymucks.models import *
from django.db.models import get_app, get_models

app = get_app('usbudget', {})
for model in get_models(app):
    databrowse.site.register(model)

urlpatterns = patterns ('',
    (r'^(.*)', databrowse.site.root),
)