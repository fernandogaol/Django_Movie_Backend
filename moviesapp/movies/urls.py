from rest_framework import routers
from .api import MovieViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, 'movies')

urlpatterns = router.urls