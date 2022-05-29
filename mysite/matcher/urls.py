from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'api/jobs', JobViewSet, basename='job')
urlpatterns = router.urls + [
    path('api-auth/', include('rest_framework.urls'))
]