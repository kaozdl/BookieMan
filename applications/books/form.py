# -*- coding: utf-8 -*-
from django.forms import ModelForm

from applications.books.models import Book, Collection

class BookForm(ModelForm):
    def __init__(self,request,*args,**kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = 'Autor'
        self.fields['name'].label = 'Nombre'
        self.fields['place_in_collection'].label = u'Lugar en la colección'
        if request.user:
            self.fields['collection'].queryset = Collection.objects.filter(user=request.user)
        self.fields['collection'].label = u'Colección'
    class Meta:
        model = Book
        fields = ['name','author','collection','place_in_collection']

class TakeBook(ModelForm):
    def __init__(self,*args,**kwargs):
        super(TakeBook, self).__init__(*args, **kwargs)
        self.fields['taker'].label = 'Usufructuario'
    class Meta:
        model = Book
        fields = ['taker']

class EditBook(ModelForm):
    def __init__(self,request,*args,**kwargs):
        super(EditBook, self).__init__(*args, **kwargs)
        self.fields['author'].label = 'Autor'
        self.fields['name'].label = 'Nombre'
        self.fields['place_in_collection'].label = u'Lugar en la colección'
        self.fields['collection'].label = u'Colección'
        if request.user:
            self.fields['collection'].queryset = Collection.objects.filter(user=request.user)
    class Meta:
        model = Book
        fields = ['name','author','collection','place_in_collection']

class CollectionForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Nombre'
        self.fields['books'].label = 'Cantidad de libros'
    class Meta:
        model = Collection
        fields = ['name','books']
