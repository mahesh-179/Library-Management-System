from django.shortcuts import render,get_object_or_404
from .models import Book
# Create your views here.
def home(request):
    return render(request,"department/home.html")

def books_display(request):
    books = Book.objects.all()
    context = {
        "books":books,
    }
    return render(request,"department/bookdisplay.html",context=context)
def borrow_books(request,id):
    book = get_object_or_404(Book,id=id)
    