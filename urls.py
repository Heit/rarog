from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^rarog/', include('rarog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^photologue/', include('photologue.urls')),
     (r'^$', include('rarog.firstpage.urls')),
     (r'^entries/', include('rarog.entries.urls')),
#     (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/firstpage', 'permanent': True}),
     (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),

      
)
