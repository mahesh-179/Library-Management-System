from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=25)
    bio = models.TextField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_name')
    isbn = models.CharField(unique=True,blank=True,null=True)
    published_date = models.DateField(blank=True,null=True)
    copies_total = models.PositiveIntegerField()
    copies_available = models.PositiveIntegerField()
    
    def is_available(self):
        return self.copies_available > 0