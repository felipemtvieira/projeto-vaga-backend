from rest_framework import serializers
from .models import Colaborador
from dependentes.models import Dependente

class ColaboradorSerializer(serializers.ModelSerializer):
    have_dependents = serializers.SerializerMethodField()

    class Meta:
        model = Colaborador
        fields = ['id', 'nome', 'departamento', 'have_dependents']

    def get_have_dependents(self, obj):
        if hasattr(obj, 'dependentes_count'):
            return obj.dependentes_count > 0
        
        return obj.dependente_set.exists()
