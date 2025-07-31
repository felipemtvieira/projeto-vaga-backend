from rest_framework import viewsets
from .models import Dependente
from .serializers import DependenteSerializer

class DependenteViewSet(viewsets.ModelViewSet):
    queryset = Dependente.objects.all()
    serializer_class = DependenteSerializer
