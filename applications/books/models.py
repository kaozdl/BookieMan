from __future__ import unicode_literals

from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=60)
    # How many books are in the collection
    books = models.IntegerField()

class Book(models.Model):
    # Core
    name = models.CharField(max_length=60)
    taken = models.BooleanField(default=False)
    taker = models.CharField(max_length=20,blank=True)
    last_take = models.DateField(blank=True)
    # Misc
    author = models.CharField(max_length=60)
    collection = models.ForeignKey(Collection,null=True)
