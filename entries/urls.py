from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import list_detail
from rarog.news.models import SiteNew
from rarog.entries.views import *

urlpatterns = patterns('',
    (r'^$', frontpage),
    (r'^photologue/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GALERY_PATH}),
)
