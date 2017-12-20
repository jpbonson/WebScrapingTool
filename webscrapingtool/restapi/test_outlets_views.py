import json
from django.urls import reverse
from .models import Outlet
from rest_framework import status
from rest_framework.test import APITestCase


class OutletTests(APITestCase):
    def setUp(self):
        Outlet.objects.create(name="WolfNews", website="wolf.com", description="dark")
        Outlet.objects.create(name="Culture", website="culture.com", description="interesting")

    def test_create_outlet(self):
        """
        Ensure we can create a new outlet object.
        """
        url = reverse('outlet-list')
        data = {'name': 'NiceNews', 'website': 'news.com', 'description': 'cool website'}
        response = self.client.post(url, data, format='json')
        result = json.loads(response.content)
        result.pop('id')
        self.assertEqual(result, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_outlets(self):
        """
        Ensure we can list outlet objects.
        """
        url = reverse('outlet-list')
        response = self.client.get(url)
        result = map(lambda x: x['name'], json.loads(response.content))
        expected = map(lambda x: x.name, list(Outlet.objects.all()))
        self.assertEqual(result, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_outlet(self):
        """
        Ensure we can get an outlet object.
        """
        sample_id = 1
        url = reverse('outlet-detail', kwargs={'outlet_id': sample_id})
        response = self.client.get(url)
        result = json.loads(response.content)
        expected = Outlet.objects.get(id=sample_id)
        self.assertEqual(result['name'], expected.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_outlet(self):
        """
        Ensure we can update an outlet object.
        """
        sample_id = 1
        url = reverse('outlet-detail', kwargs={'outlet_id': sample_id})
        data = {'name': 'NewNews', 'website': 'news2.com', 'description': ''}
        response = self.client.put(url, data, format='json')
        result = json.loads(response.content)
        expected = Outlet.objects.get(id=sample_id)
        self.assertEqual(result['name'], expected.name)
        self.assertEqual(result['website'], expected.website)
        self.assertEqual(result['description'], expected.description)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_outlet(self):
        """
        Ensure we can partially update an outlet object.
        """
        sample_id = 1
        url = reverse('outlet-detail', kwargs={'outlet_id': sample_id})
        data = {'name': 'NewNews'}
        response = self.client.patch(url, data, format='json')
        result = json.loads(response.content)
        expected = Outlet.objects.get(id=sample_id)
        self.assertEqual(result['name'], expected.name)
        self.assertEqual(result['website'], expected.website)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_outlet(self):
        """
        Ensure we can delete an outlet object.
        """
        sample_id = 1
        url = reverse('outlet-detail', kwargs={'outlet_id': sample_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, '')
        with self.assertRaises(Exception) as context:
            Outlet.objects.get(id=sample_id)
        self.assertTrue('Outlet matching query does not exist.' in context.exception)
