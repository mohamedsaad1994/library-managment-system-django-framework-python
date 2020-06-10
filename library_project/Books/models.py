from django.db import models
from Authors.models import Author

# Create your models here.
class Book(models.Model):
    PUBLISH='published'
    WITHDRAWN='withdraw'
    DRAFT='draft'
    BOOK_STATUS= [
        (PUBLISH,'Published'),
        (WITHDRAWN,'withdrawn'),
        (DRAFT,'draft'),
    ]
    name=models.CharField(max_length=30)
    status=models.CharField(max_length=10,choices=BOOK_STATUS,default=DRAFT)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_books')
