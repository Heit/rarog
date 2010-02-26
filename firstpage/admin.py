from django.contrib import admin
from rarog.firstpage.models import PageEntry, PageImage

class PageEntryAdmin(admin.ModelAdmin):
    list_display = ('dataorder', 'body_mrk')
    fieldsets = (
        (None, {'fields':('dataorder','body_mrk')}),
    )

class PageImageAdmin(admin.ModelAdmin):
    list_display = ('dataorder', 'image')
    fieldsets = (
	(None, {'fields':('dataorder','image')}),
    )


admin.site.register(PageEntry, PageEntryAdmin)
admin.site.register(PageImage, PageImageAdmin)
