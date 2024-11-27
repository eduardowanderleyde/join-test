from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TargetViewSet, map_view

# Configurar o roteador do Django REST Framework
router = DefaultRouter()
router.register(r'targets', TargetViewSet, basename='target')

urlpatterns = [
    path('', map_view, name='map'),  # Rota para o mapa
    path('api/', include(router.urls)),  # Rotas da API
]
