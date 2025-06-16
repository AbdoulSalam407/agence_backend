from rest_framework import viewsets
from .models import Proprietaire, Locataire, Logement, Contrat, Paiement
from .serializers import *

class ProprietaireViewSet(viewsets.ModelViewSet):
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer

class LocataireViewSet(viewsets.ModelViewSet):
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer

class LogementViewSet(viewsets.ModelViewSet):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer

class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer

class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
