from django.contrib import admin
from rarog.users.models import UserProfile

class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'description')


admin.site.register(UserProfile, UserAdmin)
