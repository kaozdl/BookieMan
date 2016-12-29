from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(\d+)$', views.list_book, name='book'),
    url(r'^book/$', views.list_books, name='books'),
    url(r'^collection/(\d+)$', views.list_collection, name='collection'),
    url(r'^collection/$', views.list_collections, name='collections')
]
