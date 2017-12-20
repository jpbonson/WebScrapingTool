import json
from django.urls import reverse
from restapi.models import Outlet, Author, Article
from rest_framework import status
from rest_framework.test import APITestCase


class ArticleTests(APITestCase):
    def setUp(self):
        outlet1 = Outlet.objects.create(name="WolfNews", website="wolf.com", description="dark")
        outlet2 = Outlet.objects.create(
            name="Culture", website="culture.com", description="interesting")

        author1 = Author.objects.create(name="Ana", email="ana@email.com", outlet=outlet1)
        author2 = Author.objects.create(name="Joao", email="joao@hotmail.com", outlet=outlet1)
        author3 = Author.objects.create(name="Maria", email="ma123@gmail.com", outlet=outlet2)

        Article.objects.create(
            title="Startups e o Apocalipe",
            content="iegb eigeiggeb iwe",
            publication_date='2001-12-30',
            outlet=outlet1,
            author=author1)
        Article.objects.create(
            title="A Arte de Dormir",
            content="rgg rgddrgd drhhdrhhd dr",
            publication_date='2001-12-30',
            outlet=outlet2,
            author=author1)
        Article.objects.create(
            title="New York e Eu",
            content="ssesgseg sgsegsgsgrrsgs ddsgs",
            publication_date='2001-12-30',
            outlet=outlet1,
            author=author2)
        Article.objects.create(
            title="Queijo para Todos",
            content="grdg fhdr drhdrhdhdh",
            publication_date='2001-12-30',
            outlet=outlet2,
            author=author3)

    def test_create_article(self):
        """
        Ensure we can create a new article object.
        """
        sample_outlet_id = 1
        sample_author_id = 1
        url = reverse('article-list', kwargs={'outlet_id': sample_outlet_id})
        data = {
            'title': 'Lobisomens Contra-atacam',
            'content': 'rg gergrgreherehr hergeer gerr',
            'publication_date': '2051-11-13',
            'outlet_id': sample_outlet_id,
            'author_id': sample_author_id
        }
        response = self.client.post(url, data, format='json')
        result = json.loads(response.content)
        result.pop('id')
        data.pop('outlet_id')
        data.pop('author_id')
        self.assertEqual(result, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_articles(self):
        """
        Ensure we can list article objects.
        """
        sample_outlet_id = 1
        url = reverse('article-list', kwargs={'outlet_id': sample_outlet_id})
        response = self.client.get(url)
        result = map(lambda x: x['title'], json.loads(response.content))
        expected = map(lambda x: x.title, list(Article.objects.filter(outlet_id=sample_outlet_id)))
        self.assertEqual(result, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_article(self):
        """
        Ensure we can get an article object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('article-detail', kwargs={
            'outlet_id': sample_outlet_id, 'article_id': sample_id
        })
        response = self.client.get(url)
        result = json.loads(response.content)
        expected = Article.objects.get(id=sample_id)
        self.assertEqual(result['title'], expected.title)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_article(self):
        """
        Ensure we can update an article object.
        """
        sample_id = 1
        sample_author_id = 1
        sample_outlet_id = 1
        url = reverse('article-detail', kwargs={
            'outlet_id': sample_outlet_id, 'article_id': sample_id
        })
        data = {
            'title': 'Dia Estrelado',
            'content': 'grh hr rhser hfherhsrhhr',
            'publication_date': '2022-11-14',
            'outlet_id': sample_outlet_id,
            'author_id': sample_author_id
        }
        response = self.client.put(url, data, format='json')
        result = json.loads(response.content)
        expected = Article.objects.get(id=sample_id)
        self.assertEqual(result['title'], expected.title)
        self.assertEqual(result['content'], expected.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_article(self):
        """
        Ensure we can partially update an article object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('article-detail', kwargs={
            'outlet_id': sample_outlet_id, 'article_id': sample_id
        })
        data = {'title': 'Violinos e Girafas'}
        response = self.client.patch(url, data, format='json')
        result = json.loads(response.content)
        expected = Article.objects.get(id=sample_id)
        self.assertEqual(result['title'], expected.title)
        self.assertEqual(result['content'], expected.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        """
        Ensure we can delete an article object.
        """
        sample_outlet_id = 1
        sample_id = 1
        url = reverse('article-detail', kwargs={
            'outlet_id': sample_outlet_id, 'article_id': sample_id
        })
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, '')
        with self.assertRaises(Exception) as context:
            Article.objects.get(id=sample_id)
        self.assertTrue('Article matching query does not exist.' in context.exception)
