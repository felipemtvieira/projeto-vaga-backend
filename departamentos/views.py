from rest_framework import viewsets
from .models import Departamento
from .serializers import DepartamentoSerializer
from django.db.models import Prefetch
from colaboradores.models import Colaborador
from django.db.models import Count

class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        queryset = Departamento.objects.all()
        colaboradores_param = self.request.query_params.get('colaboradores', 'false').lower()

        if colaboradores_param == 'true':
            colaboradores_com_contagem = Colaborador.objects.annotate(dependentes_count=Count('dependente'))

            print(type(colaboradores_com_contagem))
            
            queryset = queryset.prefetch_related(
                Prefetch(
                    'colaborador_set',
                    queryset=colaboradores_com_contagem
                )
            )

        return queryset
    
