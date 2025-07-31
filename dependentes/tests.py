from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Dependente
from colaboradores.models import Colaborador
from departamentos.models import Departamento

class DependenteTests(APITestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(nome='Vendas')
        self.colaborador = Colaborador.objects.create(nome='Davi', departamento=self.departamento)
        self.dependente = Dependente.objects.create(nome='Ana', colaborador=self.colaborador)

        self.list_url = reverse('dependente-list')
        self.detail_url = reverse('dependente-detail', kwargs={'pk': self.dependente.pk})
        
    def test_create_dependente(self):
        data = {'nome': 'Carlos', 'colaborador': self.colaborador.pk}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dependente.objects.count(), 2)

    def test_list_dependentes(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Ana')

    def test_retrieve_dependente(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Ana')

    def test_update_dependente(self):
        data = {'nome': 'Roberto'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dependente.refresh_from_db()
        self.assertEqual(self.dependente.nome, 'Roberto')

    def test_delete_dependente(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dependente.objects.count(), 0)
