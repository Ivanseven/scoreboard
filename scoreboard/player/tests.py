from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from scoreboard.player.models import Player

from django.contrib.auth.models import Group
class PlayerTests(APITestCase):
    fixtures = ['group.json', 'user.json', 'score.json']

    def test_list_players_endpoint(self):
        """
        Get players and their scores
        """

        url = reverse('players-list')
        response = self.client.get(url, {}, format='json')
        
        # Data from user.json & score.json
        expected_response = [
            {'player_id': 2, 'username': 'Player 1', 'score': 4},
            {'player_id': 3, 'username': 'Player 2', 'score': -1},
            {'player_id': 4, 'username': 'Player 3', 'score': 0}
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_get_player_score_endpoint(self):
        """
        Get a player's score
        """
        url = reverse('players-get_score', kwargs={'pk': 3})
        response = self.client.get(url, {}, format='json')
        
        # Data from user.json & score.json
        expected_response = {
            "id": 3,
            "username": "Player 2",
            "email": "player2@example.com",
            "score": -1
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_each_get_player_score_endpoint(self):
        """
        Get each player's score
        """
        for player in Player.objects.all():
            url = reverse('players-get_score', kwargs={'pk': player.pk})
            response = self.client.get(url, {}, format='json')
            
            # Data from user.json & score.json
            expected_response = {
                "id": player.pk,
                "username": player.username,
                "email": player.email,
                "score": player.score
            }

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, expected_response)