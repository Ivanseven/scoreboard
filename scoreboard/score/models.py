from django.db import models

from scoreboard.player.models import Player

class Score(models.Model):
    name = models.CharField(max_length=30)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)