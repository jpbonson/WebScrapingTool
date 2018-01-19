import json
from django.urls import reverse
from restapi.models import Outlet, Author
from rest_framework import status
from rest_framework.test import APITestCase


class AuthorTests(APITestCase):
    def setUp(self):
        outlet1 = Outlet.objects.create(name="WolfNews", website="wolf.com", description="dark")
        outlet2 = Outlet.objects.create(
            name="Culture", website="culture.com", description="interesting")

        Author.objects.create(name="Ana", email="ana@email.com", outlet=outlet1)
        Author.objects.create(name="Joao", email="joao@hotmail.com", outlet=outlet1)
        Author.objects.create(name="Maria", email="ma123@gmail.com", outlet=outlet2)

    def test_create_author(self):
        """
        Ensure we can create a new author object.
        """
        sample_outlet_id = 1
        url = reverse('v1:author-list', kwargs={'outlet_id': sample_outlet_id})
        data = {'name': 'Ricardo', 'email': 'ricardao@news.com', 'outlet_id': sample_outlet_id}
        response = self.client.post(url, data, format='json')
        result = json.loads(response.content.decode('utf-8'))
        result.pop('id')
        data.pop('outlet_id')
        self.assertEqual(result, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_author_for_inexistent_outlet_fails(self):
        """
        Ensure we can't create a new author if the outlet id doesn't exist.
        """
        sample_outlet_id = 11111
        url = reverse('v1:author-list', kwargs={'outlet_id': sample_outlet_id})
        data = {'name': 'Ricardo', 'email': 'ricardao@news.com', 'outlet_id': sample_outlet_id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.content.decode('utf-8'), '["Outlet id does not exist"]')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_authors(self):
        """
        Ensure we can list author objects.
        """
        sample_outlet_id = 1
        url = reverse('v1:author-list', kwargs={'outlet_id': sample_outlet_id})
        response = self.client.get(url)
        result = map(lambda x: x['name'], json.loads(response.content.decode('utf-8')))
        expected = map(lambda x: x.name, list(Author.objects.filter(outlet_id=sample_outlet_id)))
        self.assertEqual(list(result), list(expected))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_author(self):
        """
        Ensure we can get an author object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('v1:author-detail', kwargs={
            'outlet_id': sample_outlet_id, 'author_id': sample_id
        })
        response = self.client.get(url)
        result = json.loads(response.content.decode('utf-8'))
        expected = Author.objects.get(id=sample_id)
        self.assertEqual(result['name'], expected.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_author(self):
        """
        Ensure we can update an author object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('v1:author-detail', kwargs={
            'outlet_id': sample_outlet_id, 'author_id': sample_id
        })
        data = {'name': 'Joana', 'email': 'francesavior@gmail.com'}
        response = self.client.put(url, data, format='json')
        result = json.loads(response.content.decode('utf-8'))
        expected = Author.objects.get(id=sample_id)
        self.assertEqual(result['name'], expected.name)
        self.assertEqual(result['email'], expected.email)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_author(self):
        """
        Ensure we can partially update an author object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('v1:author-detail', kwargs={
            'outlet_id': sample_outlet_id, 'author_id': sample_id
        })
        data = {'name': 'Ana Paula'}
        response = self.client.patch(url, data, format='json')
        result = json.loads(response.content.decode('utf-8'))
        expected = Author.objects.get(id=sample_id)
        self.assertEqual(result['name'], expected.name)
        self.assertEqual(result['email'], expected.email)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        """
        Ensure we can delete an author object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('v1:author-detail', kwargs={
            'outlet_id': sample_outlet_id, 'author_id': sample_id
        })
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content.decode('utf-8'), '')
        with self.assertRaises(Exception) as context:
            Author.objects.get(id=sample_id)
        self.assertEqual('Author matching query does not exist.', str(context.exception))
