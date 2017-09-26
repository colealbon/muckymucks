from django.db.models import get_app, get_models
from django_muckymucks.muckymucks.models import *
from django.contrib import admin

app = get_app('muckymucks', {})
#for model in get_models(app):
    #admin.site.register(model)
    

