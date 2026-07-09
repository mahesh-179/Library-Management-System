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

def borrow(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method=='POST':
         if book.copies_available > 0:
            book.copies_available -= 1
            book.save()
    context = {
        "book":book,
    }
    return render(request,"department/book_details.html",context=context)


def update(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method=='POST':
        form = AddBook(request.POST,instance = book )
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = AddBook(instance=book)

    context={
        "form":form,
    }
    return render(request,"department/update_books.html",context=context)



def delete(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method =='POST':
        book.delete()
        return redirect('view_books')
    context = {
        "book":book,  
    }
    return render(request,"department/delete_books.html",context=context)


def return_books(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method=='POST':
        if book.copies_available < book.copies_total:
            book.copies_available += 1
            book.save()
    context = {
        "book":book,
    }
    return render(request,"department/book_details.html",context=context)


from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')

    books = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__name__icontains=query)
    )

    context = {
        "books": books,
        "query":query,
    }
    return render(request, "department/search.html", context)