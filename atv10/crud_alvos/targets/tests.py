from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Target

class TargetAPITestCase(TestCase):
    def setUp(self):
        # Configure the client for testing
        self.client = Client()

        # Data for a target
        self.target_data = {
            "identifier": "T001",
            "name": "Recife",
            "latitude": -8.0476,
            "longitude": -34.877,
            "expiration_date": "2024-12-31"
        }

        # Create an initial target for testing
        self.target = Target.objects.create(**self.target_data)

        # URLs for the API endpoints
        self.list_url = reverse('target-list')  # targets/api/targets/
        self.detail_url = reverse('target-detail', args=[self.target.id])  # targets/api/targets/<id>/

    def test_get_all_targets(self):
        # Test to list all targets
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_create_target(self):
        # Test to create a new target
        new_target_data = {
            "identifier": "T002",
            "name": "São Paulo",
            "latitude": -23.55052,
            "longitude": -46.633308,
            "expiration_date": "2025-12-31"
        }
        response = self.client.post(self.list_url, data=new_target_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Target.objects.count(), 2)

    def test_update_target(self):
        # Test to update an existing target
        updated_data = {
            "identifier": "T003",
            "name": "Novo Nome",
            "latitude": -9.0476,
            "longitude": -35.877,
            "expiration_date": "2026-12-31"
        }
        response = self.client.put(self.detail_url, data=updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.target.refresh_from_db()
        self.assertEqual(self.target.name, "Novo Nome")

    def test_delete_target(self):
        # Test to delete an existing target
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Target.objects.count(), 0)

    def test_map_view(self):
        # Test to verify that the map page loads correctly
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Mapa de Alvos")  # Checks if the map title is present
