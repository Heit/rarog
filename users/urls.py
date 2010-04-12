from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import list_detail
from django.views.generic.list_detail import object_detail
from rarog.users.models import *

info_dict = {
	'profiles': UserProfile.objects.all(),
}


urlpatterns = patterns('django.views.generic.simple',
    (r'^$','direct_to_template', {'template': 'users/list.html', 'extra_context': info_dict}),
)


