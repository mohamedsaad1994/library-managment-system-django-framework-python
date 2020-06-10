from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView,DeleteView,UpdateView,CreateView
from .filters import BookFilter

# Create your views here.
def books(request):
    books = Book.objects.all()
    myFilter= BookFilter(request.GET ,queryset=books)
    books=myFilter.qs
    return render(request,'Books/books.html',{"books":books ,'myFilter':myFilter})

class BookDetail(DetailView):
    model=Book

class BookDelete(DeleteView):
    model=Book
    success_url='/'

class BookUpdate(UpdateView):
    model=Book
    success_url='/' 
    fields = ['name','author','status']
    template_name_suffix = '_update_form' 

class BookCreate(CreateView):
    model=Book
    success_url='/' 
    fields = ['name','author','status']
    template_name_suffix = '_update_form'   