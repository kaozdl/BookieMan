from django.shortcuts import render
from django.http import HttpResponse

from BookieMan.applications.books.models import Book, Collection

def mark_as_taken(request):
    # tkn = Averiguar como se mandan y reciben parámetros a traves del template
    if tkn.taken == False:
        tkn.taker = request.taker
        tkn.taken = True
        tkn.save()
        return HttpResponse("Prestado Correctamente")
    else:
        return HttpResponse("Este libro se encuentra prestado")

def untake(request):
    # untk = Averiguar como se consiguen los objetos
    untk.taker = ""
    untk.save()
    return HttpResponse("Devuelto Correctamente")

def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,books,context)

def list_book(request):
    book = Book.objects.get(id=book__id)
    context = {'book': book}
    return render(request,book,context)

def list_collections(request):
    collections = Collection.objects.all()
    context = {'collections': collections}
    return render(request,collections,context)

def list_collection(request):
    collection = Book.objects.filter(collection=collection)
    context = {'collection': collection}
    return render(request,collection,context)

def addToCollection(request):
    # bookToAdd = Averiguar como se consiguen los objetos
    if bookToAdd.collection != None
        return HttpResponse ("Este libro se encuentra en: "+bookToAdd.collection)
    elif (Collection.objects.filter(id=collection_id).count() > 0):
        bookToAdd.collection = collection_id
        bookToAdd.save()
        return HttpResponse("Operacion Exitosa")
    else:
        return HttpResponse(u"La colección no existe")
