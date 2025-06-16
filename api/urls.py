from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'proprietaires', ProprietaireViewSet)
router.register(r'locataires', LocataireViewSet)
router.register(r'logements', LogementViewSet)
router.register(r'contrats', ContratViewSet)
router.register(r'paiements', PaiementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
