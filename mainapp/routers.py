from rest_framework.routers import DefaultRouter
from api.viewsets import GetViewSet
router = DefaultRouter()

router.register(r'get',GetViewSet,basename='get')