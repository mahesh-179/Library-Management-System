from django import forms 
from .models import Author,Book

class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        
        
class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'