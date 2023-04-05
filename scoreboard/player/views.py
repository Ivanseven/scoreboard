from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from scoreboard.player.serializers import PlayerScoreSerializer, UserSerializer, GroupSerializer
from scoreboard.player.models import Player

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlayerViewSet(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []

    def list(self, request, format=None):
        """
        Return a list of all players & their scores
        """
        # Exclude staff users from the output
        player_scores = [ {'player_id': player.id, 'username': player.username, 'score':player.score} for player in Player.objects.filter(is_staff=False)]

        return Response(player_scores)
    
    @action(detail=True,url_name='get_score', methods=['get'])    
    def get_score(self, request, format=None, pk=None):
        
        player = Player.objects.filter(is_staff=False, pk=pk).first()
        serializer = PlayerScoreSerializer(player)
    
        return Response(serializer.data)