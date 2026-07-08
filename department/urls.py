from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('view_books',views.books_display,name="view_books"),
    
]
