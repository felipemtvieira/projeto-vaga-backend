from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Departamento

class DepartamentoTests(APITestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(nome='RH')
        self.list_url = reverse('departamento-list')
        self.detail_url = reverse('departamento-detail', kwargs={'pk': self.departamento.pk})

    def test_create_departamento(self):
        data = {'nome': 'Financeiro'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Departamento.objects.count(), 2)

    def test_list_departamentos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'RH')

    def test_retrieve_departamento(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'RH')

    def test_update_departamento(self):
        data = {'nome': 'Recursos Humanos'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.departamento.refresh_from_db()
        self.assertEqual(self.departamento.nome, 'Recursos Humanos')

    def test_delete_departamento(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Departamento.objects.count(), 0)

    def test_cannot_create_with_existing_name(self):
        data = {'nome': 'RH'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
