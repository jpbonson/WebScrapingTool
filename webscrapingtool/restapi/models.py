from __future__ import unicode_literals
from django.db import models


class Outlet(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Author(models.Model):
    outlet = models.ForeignKey(Outlet, related_name='author_outlets', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    profile_page = models.CharField(max_length=255, null=True)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Article(models.Model):
    outlet = models.ForeignKey(Outlet, related_name='article_outlets', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='article_authors', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, null=True)
    publication_date = models.DateField()

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
