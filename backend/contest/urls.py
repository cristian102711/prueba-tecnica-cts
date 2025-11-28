from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConcursoViewSet

router = DefaultRouter()
router.register(r'participantes', ConcursoViewSet, basename='participante')

urlpatterns = [
    path('', include(router.urls)),
]