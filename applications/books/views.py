# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from applications.books.models import Book, Collection

def index(request):
    context = {}
    return render(request,'index.html',context)

def mark_as_taken(request,bookid):
    tkn = Book.objcects.get(id=bookid)
    if (tkn.taken == False):
        tkn.taker = request.taker
        tkn.taken = True
        tkn.save()
        return HttpResponse("Prestado Correctamente")
    else:
        return HttpResponse("Este libro se encuentra prestado")

def untake(request,bookid):
    untk = Book.objects.get(id=bookid)
    if (untk.taken == True):
        untk.taker = ""
        untk.save()
        return HttpResponse("Devuelto Correctamente")
    else:
        return HttpResponse("Este libro no se encuentra prestado")

def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'books.html',context)

def list_book(request,bookid):
    # import ipdb; ipdb.set_trace()
    book = Book.objects.get(id=bookid)
    name = book.name
    author = book.author
    if (book.taken == True):
        state = 'Prestado'
    else:
        state = 'En el estante'
    if (book.collection != None):
        collection = book.collection.name
    else:
        collection = ""
    context = {'name': name, 'author' : author, 'state': state, 'collection' : collection}
    return render(request,'book.html',context)

def delete_book(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    return HttpResponse("Borrado exitosamente")

def list_collections(request):
    collections = Collection.objects.all()
    context = {'collections': collections}
    return render(request,'collections.html',context)

def list_collection(request,collection):
    collection = Book.objects.filter(collection=collection)
    name = Collection.objects.get(collection=collection).name
    count = collection.count()
    context = {'collection': collection, 'name': name, 'count': count}
    return render(request,'collection.html',context)

def addToCollection(request):
    # bookToAdd = Averiguar como se consiguen los objetos
    if bookToAdd.collection != None:
        return HttpResponse ("Este libro se encuentra en: "+bookToAdd.collection)
    elif (Collection.objects.filter(id=collection_id).count() > 0):
        bookToAdd.collection = collection_id
        bookToAdd.save()
        return HttpResponse("Operacion Exitosa")
    else:
        return HttpResponse(u"La colección no existe")
