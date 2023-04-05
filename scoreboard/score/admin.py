from django.contrib import admin

from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'value', 'created_at']
    search_fields = ['user__username', 'name', 'value', ]

admin.site.register(Score, ScoreAdmin)