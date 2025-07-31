from rest_framework import viewsets
from .models import Colaborador
from .serializers import ColaboradorSerializer
from django.db.models import Count
from dependentes.models import Dependente

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.annotate(
        dependentes_count=Count('dependente')
    )
    serializer_class = ColaboradorSerializer
