from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    # Core
    name = models.CharField(max_lenght=60)
    taken = models.BooleanField(default=False)
    taker = models.CharField(max_lenght=20)
    last_take = models.DateField()
    # Misc
    author = models.CharField(max_lenght=60)
    collection = models.ForeignKey(Collection)

class Collection(models.Model):
    name = models.CharField(max_lenght=60)
    books = models.IntegerField()
