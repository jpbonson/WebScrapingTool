from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^outlets/$',
        views.OutletList.as_view(),
        name='outlet-list'
    ),
    url(
        r'^outlets/(?P<outlet_id>[0-9]+)/$',
        views.OutletDetail.as_view(),
        name='outlet-detail'
    ),
    url(
        r'^outlets/(?P<outlet_id>[0-9]+)/authors/$',
        views.AuthorList.as_view(),
        name='author-list'
    ),
    url(
        r'^outlets/(?P<outlet_id>[0-9]+)/authors/(?P<author_id>[0-9]+)/$',
        views.AuthorList.as_view(),
        name='author-detail'
    ),
]
