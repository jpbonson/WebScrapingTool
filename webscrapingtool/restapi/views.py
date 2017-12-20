from rest_framework import generics
from .models import Outlet, Author
from .serializers import OutletSerializer, AuthorSerializer


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
        serializer.save(outlet_id=self.kwargs['outlet_id'])

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
