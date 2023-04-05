from django.urls import path

from .. import views

app_name = 'players'

urlpatterns = [
    path('get_score', views.ListPlayerScores.as_view(), name='get_score'),
]