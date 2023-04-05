from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0) # TODO: rename this column to value in demo
    created_at = models.DateTimeField(auto_now_add=True)