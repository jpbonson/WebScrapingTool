from .models import Outlet, Author, Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'link', 'content', 'publication_date', 'tags', 'author_id')


class AuthorSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'articles')


class OutletSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Outlet
        fields = ('id', 'name', 'website', 'description', 'authors', 'articles')
