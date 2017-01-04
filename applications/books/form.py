from django.forms import ModelForm

from applications.books.models import Book, Collection

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','author','collection']

class TakeBook(ModelForm):
    class Meta:
        model = Book
        fields = ['taker']

class AddToCollection(ModelForm):
    class Meta:
        model = Book
        fields = ['collection']

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['name','books']
