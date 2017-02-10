from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
# AUTH VIEWS
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
# MY VIEWS
    url(r'^$', views.index, name='index'),
    url(r'^book/([0-9]+)$', views.list_book, name='book'),
    url(r'^book/$', views.list_books, name='books'),
    url(r'^collection/([0-9]+)$', views.list_collection, name='collection'),
    url(r'^collection/$', views.list_collections, name='collections'),
    url(r'^deletebook/([0-9]+)$', views.delete_book, name='bookdlt'),
    url(r'^untakebook/([0-9]+)$', views.untake, name='bookuntk'),
    url(r'^takebook/([0-9]+)$', views.mark_as_taken, name='booktk'),
    url(r'^editbook/([0-9]+)$', views.edit_book, name='editbook'),
    url(r'^booknew/$', views.new_book, name='newbook'),
    url(r'^collectionnew/$', views.new_collection, name='newcollection'),
    url(r'^collectionedit/([0-9]+)$', views.edit_collection, name='collectionEdit')
]
