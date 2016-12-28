from django.forms import ModelForm

from BookieMan.books.models import Book, Collection

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','taker','collection']

class Collection(ModelForm):
    class Meta:
        model = Collection
        fields = ['name','books']
