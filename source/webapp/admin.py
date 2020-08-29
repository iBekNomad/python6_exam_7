from django.contrib import admin
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer)
