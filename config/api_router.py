from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from quest_meme.users.viewsets import *

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("cookie", CookieViewSet)
router.register("meme", MemeViewSet, basename='meme')

# user_details


app_name = "api"
urlpatterns = router.urls