from django.contrib import admin
from rarog.entries.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','enable_comments','status')
    search_fields = ['title','body_markdown']
    list_filter = ('pub_date','enable_comments','status')
    prepopulated_fields = {"slug":('title',)}
    fieldsets = (
        (None, {'fields':(('title','status'),'body_markdown',('pub_date','enable_comments'),'tags','slug','image')}),
    )

admin.site.register(Entry, EntryAdmin)
