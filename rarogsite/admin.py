from django.contrib import admin
from rarog.rarogsite.models import Entry, RarogUser, FirstPageEntry, FirstPageImage

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','enable_comments','status')
    search_fields = ['title','body_markdown']
    list_filter = ('pub_date','enable_comments','status')
    prepopulated_fields = {"slug":('title',)}
    fieldsets = (
        (None, {'fields':(('title','status'),'body_markdown',('pub_date','enable_comments'),'tags','slug')}),
    )

class RarogUserAdmin(admin.ModelAdmin):
    pass

class FirstPageEntryAdmin(admin.ModelAdmin):
    list_display = ('dataorder', 'body_mrk')
    fieldsets = (
        (None, {'fields':('dataorder','body_mrk')}),
    )

class FirstPageImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
admin.site.register(RarogUser, RarogUserAdmin)
admin.site.register(FirstPageEntry, FirstPageEntryAdmin)
admin.site.register(FirstPageImage, FirstPageImageAdmin)
