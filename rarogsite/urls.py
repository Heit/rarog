from django.conf.urls.defaults import *
from rarog.rarogsite.models import Entry
from tagging.views import tagged_object_list

info_dict = {
        'queryset': Entry.objects.filter(status=1),
        'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'(?P<year>\d{4}/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, slug_field='slug', template_name='rarogsite/detail.html')), 
)
