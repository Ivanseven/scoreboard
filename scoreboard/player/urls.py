from rest_framework import routers
from scoreboard.player import views as PlayerViews

app_name = 'players'

router = routers.DefaultRouter()
router.register(r'users', PlayerViews.UserViewSet)
router.register(r'groups', PlayerViews.GroupViewSet)
router.register(r'players', PlayerViews.PlayerViewSet, basename='players')