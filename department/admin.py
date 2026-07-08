from django.contrib import admin
from .models import Author,Book
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display =['name','bio','date_of_birth']
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=['title','published_date','copies_available']
    
admin.site.register(Book,BookAdmin)