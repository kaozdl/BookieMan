# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from applications.books.models import Book, Collection
from applications.books.form import BookForm, CollectionForm, TakeBook, EditBook

@login_required(login_url='login')
def index(request):
    context = {}
    return render(request,'index.html',context)

@login_required(login_url='login')
def new_book(request):
    if request.method == 'POST':
        newbook = BookForm(request.POST)
        if newbook.is_valid():
            newbook = Book()
            newbook.name = request.POST['name']
            newbook.author = request.POST['author']
            if request.POST['collection'] == '':
                newbook.collection = None
            else:
                newbook.collection = Collection.objects.get(id=int(request.POST['collection']))
            newbook.user = request.user
            newbook.save()
            book = BookForm()
            context = {'form': book}
            return render(request,'bookCreate.html',context)
        else:
            return HttpResponse('Datos incorrectos')
    else:
        book = BookForm()
        context = {'form': book}
        return render(request,'bookCreate.html',context)

@login_required(login_url='login')
def edit_book(request,bookid):
    if request.method == 'POST':
        book = Book.objects.get(id=bookid)
        book.name = request.POST['name']
        book.author = request.POST['author']
        if request.POST['collection'] == '':
            book.collection = None
        else:
            book.collection = Collection.objects.get(id=int(request.POST['collection']))
        book.save()
        return list_book(request,bookid)
    else:
        pbook = Book.objects.get(id=bookid)
        book = EditBook(initial={'name':pbook.name, 'collection':pbook.collection, 'author':pbook.author,})
        context = {'form' : book ,'pbook':pbook}
        return render(request,'bookEdit.html',context)

@login_required(login_url='login')
def new_collection(request):
    if request.method == 'POST':
        newcollection = CollectionForm(request.POST)
        if newcollection.is_valid():
            newcollection = Collection
            newcollection.user = request.user
            newcollection.name = request.POST['name']
            newcollection.books = request.POST['books']
            newcollection.save()
            collection = CollectionForm()
            context = {'form': collection}
            return render(request,'collectionCreate.html',context)
        else:
            return HttpResponse('Datos incorrectos')
    else:
        book = CollectionForm()
        context = {'form': book}
        return render(request,'collectionCreate.html',context)

@login_required(login_url='login')
def mark_as_taken(request,bookid):
    # import ipdb; ipdb.set_trace()
    book = Book.objects.get(id=bookid)
    if (request.method == 'POST') and (book.taken == False):
        book.taker = request.POST['taker']
        book.taken = True
        book.save()
        return list_book(request,bookid)
    elif (request.method == 'GET') and (book.taken == False):
        book = TakeBook(request.GET)
        context = {'form': book}
        return render(request,'bookTake.html',context)
    else:
        return list_books(request,message='Este libro se encuentra prestado')

@login_required(login_url='login')
def untake(request,bookid):
    untk = Book.objects.get(id=bookid)
    if (untk.taken == True):
        untk.taker = ""
        untk.taken = False
        untk.save()
        return list_books(request,message="Devuelto Correctamente")
    else:
        return list_books(request,message="Este libro no se encuentra prestado")

@login_required(login_url='login')
def list_books(request,*args,**kwargs):
    books = Book.objects.filter(user=request.user)
    if kwargs.get('message') != None:
        context = {'books': books , 'message':kwargs.get('message')}
    else:
        context = {'books':books}
    return render(request,'books.html',context)

@login_required(login_url='login')
def list_book(request,bookid):
    # import ipdb; ipdb.set_trace()
    book = Book.objects.get(id=bookid)
    name = book.name
    author = book.author
    taker = book.taker
    if (book.taken == True):
        state = 'Prestado'
    else:
        state = 'En el estante'
    if (book.collection != None):
        collection = book.collection.name
    else:
        collection = ""
    context = {'name': name, 'author' : author, 'state':state, 'taker': taker, 'collection' : collection}
    return render(request,'book.html',context)

@login_required(login_url='login')
def delete_book(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    return list_books(request,message='Borrado Exitosamente')

@login_required(login_url='login')
def list_collections(request):
    collections = Collection.objects.filter(user=request.user)
    context = {'collections': collections}
    return render(request,'collections.html',context)

@login_required(login_url='login')
def list_collection(request,collection):
    collection = Book.objects.filter(collection=collection)
    name = Collection.objects.get(collection=collection).name
    count = collection.count()
    context = {'collection': collection, 'name': name, 'count': count}
    return render(request,'collection.html',context)
