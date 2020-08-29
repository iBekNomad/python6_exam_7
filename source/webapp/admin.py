from django.contrib import admin
from webapp.models import Poll


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')


admin.site.register(Poll, PollAdmin)
