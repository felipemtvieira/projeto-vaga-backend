from rest_framework import serializers
from .models import Dependente

class DependenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependente
        fields = ['id', 'nome', 'colaborador']
