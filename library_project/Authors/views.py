from django.shortcuts import render
from .models import Author 
from Books.models import Book
from django.views.generic import DetailView,DeleteView,UpdateView,CreateView
from .filters import AuthorFilter

# Create your views here.
def authors(request):
    authors = Author.objects.all()
    myFilter= AuthorFilter(request.GET ,queryset=authors)
    authors=myFilter.qs
    return render(request,'Authors/authors.html',{"authors":authors ,'myFilter':myFilter})

class AuthorDetail(DetailView):
    model=Author


class AuthorDelete(DeleteView):
    model=Author
    success_url='/'

class AuthorUpdate(UpdateView):
    model=Author
    success_url='/' 
    fields = ['name','nationality']
    template_name_suffix = '_update_form' 

class AuthorCreate(CreateView):
    model=Author
    success_url='/' 
    fields = ['name','nationality']
    template_name_suffix = '_update_form'   