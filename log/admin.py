from django.contrib import admin
from django.contrib.auth.models import Group
from django.conf import settings

from .models import Activity, Log

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class LogAdmin(admin.ModelAdmin):
    list_display = ['activity', 'when', 'remark', 'author']
    list_filter = ('activity',)
    exclude = ['author',]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Log, LogAdmin)

admin.site.unregister(Group)

admin.site.site_header = f"{settings.BABY_NAME} App"
admin.site.site_title = f"{settings.BABY_NAME} App"
admin.site.index_title = f"Welcome to {settings.BABY_NAME} App"
