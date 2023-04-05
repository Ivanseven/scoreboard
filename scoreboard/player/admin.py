from django.contrib import admin

from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username', 'score']
    search_fields = ['username',]

admin.site.register(Player, PlayerAdmin)