from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import AddAuthor,AddBook
# Create your views here.
def home(request):
    return render(request,"department/home.html")

def books_display(request):
    books = Book.objects.all()
    context = {
        "books":books,
    }
    return render(request,"department/bookdisplay.html",context=context)

def add_author(request):
    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddAuthor()
    context = {
        "form":form,
    }
    return render(request,"department/add_author.html",context=context)


def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBook()
    context = {
        "form":form,
    }
    return render(request,"department/add_books.html",context=context)

def book_details(request,id):
    book = get_object_or_404(Book,id=id)
    context = {
        "book":book,
    }
    return render(request,"department/book_details.html",context=context)