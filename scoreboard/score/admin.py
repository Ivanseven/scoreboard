from django.contrib import admin

from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'score', 'created_at']
    search_fields = ['user__username', 'name', 'score', ]

admin.site.register(Score, ScoreAdmin)