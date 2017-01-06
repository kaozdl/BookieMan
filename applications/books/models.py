from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    # How many books are in the collection
    books = models.IntegerField()

    def __unicode__(self):
        return self.name

    def count_books(self):
        return Book.objects.filter(collection=self).count()

class Book(models.Model):
    # Core
    user = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    taken = models.BooleanField(default=False)
    taker = models.CharField(max_length=20,blank=True)
    last_take = models.DateField(null=True,blank=True)
    # Misc
    author = models.CharField(max_length=60)
    collection = models.ForeignKey(Collection,null=True,blank=True)
    place_in_collection = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.name
