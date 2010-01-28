from django.contrib import admin
from rarog.news.models import SiteNew
from django.utils.translation import ugettext as _

class SiteNewAdmin(admin.ModelAdmin):
    list_display = ('pubdate', 'title', 'descriptn')
    fieldsets = (
        (None, {
		'fields':('title','descriptn')
	}),
	(_('Advanced options'), {
	 	'classes': ('collapse',),
		'fields': ('eventdate', 'organizer', 'orgsite')
	}),
    )


admin.site.register(SiteNew, SiteNewAdmin)
