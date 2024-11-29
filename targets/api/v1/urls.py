from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TargetViewSet, map_view

# Configure the Django REST Framework router
router = DefaultRouter()
router.register(r'targets', TargetViewSet, basename='target')

urlpatterns = [
    path('', map_view, name='map'),  # Route to map
    path('api/', include(router.urls)),  # API routes
]
