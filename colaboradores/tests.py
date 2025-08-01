# colaboradores/tests.py (código de teste)
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Colaborador
from departamentos.models import Departamento
from dependentes.models import Dependente
from django.db.models import Count

class ColaboradorTests(APITestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(nome='TI')
        self.colaborador1 = Colaborador.objects.create(nome='Alice', departamento=self.departamento)
        self.colaborador2 = Colaborador.objects.create(nome='Bruno', departamento=self.departamento)
        Dependente.objects.create(nome='Carol', colaborador=self.colaborador1)

        self.list_url = reverse('colaborador-list')
        self.detail_url = reverse('colaborador-detail', kwargs={'pk': self.colaborador2.pk})

    def test_list_colaboradors(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['nome'], 'Alice')

    def test_retrieve_colaborador(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Bruno')

    def test_update_colaborador(self):
        data = {'nome': 'Clarice'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.colaborador2.refresh_from_db()
        self.assertEqual(self.colaborador2.nome, 'Clarice')

    def test_delete_colaborador(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Colaborador.objects.count(), 1)

    def test_list_colaboradores_with_have_dependents(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.json()
        
        self.assertTrue(any(c['nome'] == 'Alice' and c['have_dependents'] for c in data))
        self.assertTrue(any(c['nome'] == 'Bruno' and not c['have_dependents'] for c in data))
