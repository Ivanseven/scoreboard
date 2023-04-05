from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from scoreboard.player.serializers import UserSerializer, GroupSerializer
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

class ListPlayerScores(APIView):
    """
    View to list all users in the system.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all players & their scores
        """
        # Exclude staff users from the output
        player_scores = [ {'player_id': player.id, 'username': player.username, 'score':player.score} for player in Player.objects.filter(is_staff=False)]

        return Response(player_scores)