from django.contrib import admin

from applications.books.models import Book, Collection

admin.site.register(Book)
admin.site.register(Collection)
