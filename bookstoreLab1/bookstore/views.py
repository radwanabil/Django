from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Book
from .forms import BookForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    all_books = Book.objects.all()
    return render(request, 'bookstore_list.html', context={"books": all_books})

bookstore_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Harry potter',
        'price': 100,
        'description': "Learning Learnin gJSfffjk dfjdklg jkdgjdkgjdkgjd kgjdkgjdglk jdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgekLearningJSfffjkdfjdklgjkdgjdkgjdkgjdkgjdkgjdglkjdgkljfjfjejekgjekgjekgjekgjgekjgek",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'harry potter',
        'price': 400,
        'description': "Learning LearningJS fffjkdfjd klgjkdgjdkgjdkgjdkgjd kgjdglkjdgk ljfj fjejekgjekgjekgjekgjgekjgek",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Harry potter 3',
        'price': 200,
        'description': "LearningJS fffjk dfjdklgjkdg jdkgjdkgjd kgjdkgjdglkjdgkl jfjfjejekg jekgjekgjekgjgekjgek",
    },
]


def bookstore_details(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book = Book.objects.get(pk=book_id)
    return render(request, 'bookstore_details.html', context={"book": book})

def bookstore_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    Book.objects.get(pk=book_id).delete()
    return redirect("bookstore:bookstore-list")

def bookstore_update(request, **kwargs):
    book_id = kwargs.get('book_id') 
    book = Book.objects.get(pk=book_id)
    form = BookForm(instance=book)
    if request.method == "PUT":
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:bookstore-details", pk=book.id)
        
    return render(request, 'bookstore_update.html', context={
        'form': form, 
        'book': book
    })

def create_new_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookstore:bookstore-list")
    return render(request, 'bookstore_create.html', context={
        'form': form
    })