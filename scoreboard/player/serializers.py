from django.contrib.auth.models import User, Group
from rest_framework import serializers

from scoreboard.player.models import Player


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'url']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'url']

class PlayerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'email', 'score']