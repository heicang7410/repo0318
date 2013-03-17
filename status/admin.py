#encoding: utf-8

from datetime import datetime
from django.contrib import admin
from status.models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'ntime')
    search_fields = ('text', )
    list_filter = ('user', )
    date_hierarchy = 'time'

    def ntime(self, obj):
        return datetime.now() - obj.time.replace(tzinfo=None)
        #return obj.time.strftime('%Y-%m-%d %H:%M:%S')
    ntime.short_description = u'时间'

admin.site.register(Status, StatusAdmin)
