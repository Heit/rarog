from django.conf.urls.defaults import *
from django.conf import settings
#from django.views.generic import list_detail
from rarog.firstpage.models import PageEntry, PageImage
from rarog.news.models import SiteNew
from rarog.users.models import UserProfile
from rarog.firstpage.views import index

urlpatterns = patterns('',
    (r'^$', index),
    (r'^photologue/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GALERY_PATH}),
)
