from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import list_detail
from django.views.generic.list_detail import object_detail
from rarog.news.models import SiteNew
from rarog.entries.views import *

info_dict = {
	'queryset': Entry.objects.filter(status=1),
	'date_field': 'pub_date',
}


urlpatterns = patterns('',
    (r'^$', frontpage),
    (r'^photologue/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GALERY_PATH}),
    (r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(info_dict, slug_field='slug',template_name='entries/detail.html')),
    (r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(info_dict, slug_field='slug',template_name='entries/detail.html')),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(info_dict, template_name='blog/list.html')),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$','archive_day',dict(info_dict,template_name='blog/list.html')),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(info_dict, template_name='blog/list.html')),
	(r'^(?P<year>\d{4})/$','archive_year', dict(info_dict, template_name='blog/list.html')),
	(r'^$','archive_index', dict(info_dict, template_name='blog/list.html')),
)


