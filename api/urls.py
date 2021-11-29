from django.contrib.admin.sites import DefaultAdminSite
from api.views import GenreViewSet, MovieViewSet, ReviewSet, UserviewSet

from rest_framework import routers, urlpatterns

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'user', UserviewSet)
router.register(r'recommendation', GenreViewSet, basename='recommendation')
router.register(r'review', ReviewSet, basename='review')

urlpatterns = router.urls