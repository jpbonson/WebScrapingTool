from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import Outlet, Author, Article
from .serializers import OutletSerializer, AuthorSerializer, ArticleSerializer


# GET  outlets/: return a list of Outlets
# POST outlets/: create a Outlet
class OutletList(generics.ListCreateAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    lookup_url_kwarg = 'outlet_id'


# GET    outlets/<outlet_id>/: return a Outlet
# PUT    outlets/<outlet_id>/: update a Outlet
# PATCH  outlets/<outlet_id>/: patch a Outlet
# DELETE outlets/<outlet_id>/: delete a Outlet
class OutletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    lookup_url_kwarg = 'outlet_id'


# GET  outlets/<outlet_id>/authors/: return a list of Authors
# POST outlets/<outlet_id>/authors/: create a Author
class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    lookup_url_kwarg = 'outlet_id'

    def perform_create(self, serializer):
        outlet_id = self.kwargs['outlet_id']
        if not Outlet.objects.filter(id=outlet_id).exists():
            raise ValidationError("Outlet id does not exist")
        serializer.save(outlet_id=outlet_id)

    def get_queryset(self):
        outlet = self.kwargs['outlet_id']
        return Author.objects.filter(outlet__id=outlet)


# GET    outlets/<outlet_id>/authors/<author_id>/: return a Author
# PUT    outlets/<outlet_id>/authors/<author_id>/: update a Author
# PATCH  outlets/<outlet_id>/authors/<author_id>/: patch a Author
# DELETE outlets/<outlet_id>/authors/<author_id>/: delete a Author
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    lookup_url_kwarg = 'author_id'

    def get_queryset(self):
        author = self.kwargs['author_id']
        return Author.objects.filter(id=author)


# GET  outlets/<outlet_id>/articles/: return a list of Articles
# POST outlets/<outlet_id>/articles/: create a Article
class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    lookup_url_kwarg1 = 'outlet_id'

    def perform_create(self, serializer):
        def save_article(outlet_id, author_id):
            try:
                serializer.save(outlet_id=outlet_id, author_id=author_id)
            except IntegrityError:
                raise ValidationError("Article must be unique given the same outlet and author")

        def check_and_save_for_author_id():
            author_id = self.request.data['author_id']
            if not Author.objects.filter(id=author_id).exists():
                raise ValidationError("Author id does not exist")
            save_article(outlet_id, author_id)

        def check_and_save_for_author_name():
            author = self.request.data['author']
            result = Author.objects.filter(name=author).values()
            if not result.exists():
                author_id = Author.objects.create(name=author, outlet_id=outlet_id).id
            else:
                author_id = result[0]['id']
            save_article(outlet_id, author_id)

        outlet_id = self.kwargs['outlet_id']
        outlet = Outlet.objects.filter(id=outlet_id)
        if not outlet.exists():
            raise ValidationError("Outlet id does not exist")
        if 'author_id' in self.request.data:
            check_and_save_for_author_id()
        elif 'author' in self.request.data:
            check_and_save_for_author_name()
        else:
            raise ValidationError("Must inform either 'author_id' or 'author'")

    def get_queryset(self):
        outlet = self.kwargs['outlet_id']
        return Article.objects.filter(outlet__id=outlet)


# GET    outlets/<outlet_id>/articles/<article_id>/: return a Article
# PUT    outlets/<outlet_id>/articles/<article_id>/: update a Article
# PATCH  outlets/<outlet_id>/articles/<article_id>/: patch a Article
# DELETE outlets/<outlet_id>/articles/<article_id>/: delete a Article
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'article_id'

    def get_queryset(self):
        article = self.kwargs['article_id']
        return Article.objects.filter(id=article)
