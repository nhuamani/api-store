from django.conf.urls import url, include
from rest_framework import routers

from .views import LibroViewSet, AutorViewSet, IdiomaViewSet, PaisViewSet, EditorialViewSet


router = routers.DefaultRouter()

# Router public

router.register(r'libro', LibroViewSet)
router.register(r'autor', AutorViewSet)
router.register(r'idioma', IdiomaViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'editorial', EditorialViewSet)


# Router private


urlpatterns = [
    url(r'^', include(router.urls)),
]