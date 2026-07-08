from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('view_books',views.books_display,name="view_books"),
    path('add_books/',views.add_book,name='add_book'),
    path('add_author/',views.add_author,name="add_author"),
    path('book_details/<int:id>/',views.book_details,name="details"),
    path('borrow/<int:id>/',views.borrow,name="borrow"),
    
]
