from django.conf.urls.defaults import *

urlpatterns = patterns ('',
    (r'^(.*)', admin.site.root),
)
