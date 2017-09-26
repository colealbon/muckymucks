from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django_muckymucks.usbudget.models import *
from django_muckymucks.usbudget.views import *

from django.http import Http404
from django.shortcuts import render_to_response