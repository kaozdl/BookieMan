from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/([0-9]+)$', views.list_book, name='book'),
    url(r'^book/$', views.list_books, name='books'),
    url(r'^collection/([0-9]+)$', views.list_collection, name='collection'),
    url(r'^collection/$', views.list_collections, name='collections'),
    url(r'^deletebook/([0-9]+)$', views.delete_book, name='bookdlt'),
    url(r'^untakebook/([0-9]+)$', views.untake, name='bookuntk'),
    url(r'^takebook/([0-9]+)$', views.mark_as_taken, name='booktk'),
    url(r'^booknew/$', views.new_book, name='newbook'),
    url(r'^collectionnew/$', views.new_collection, name='newcollection')
]
