from rest_framework import serializers
from .models import Departamento
from colaboradores.serializers import ColaboradorSerializer

class DepartamentoSerializer(serializers.ModelSerializer):
    colaboradores = serializers.SerializerMethodField()

    class Meta:
        model = Departamento
        fields = ['id', 'nome', 'colaboradores']

    def get_colaboradores(self, obj):
        request= self.context.get('request')
        
        if request and request.query_params.get('colaboradores','false').lower() == 'true':
            colaboradores_do_departamento = obj.colaborador_set.all()

            return ColaboradorSerializer(colaboradores_do_departamento, many=True).data

        return []
