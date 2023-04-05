from rest_framework import serializers

from scoreboard.score.models import Score


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ['id','name','user','score','created_at', 'url']

