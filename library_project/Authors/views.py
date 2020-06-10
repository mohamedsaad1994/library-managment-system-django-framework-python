from django.shortcuts import render ,get_object_or_404
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

def author_detail(request,pk):
    author=get_object_or_404(Author,pk=pk)
    books=Book.objects.filter(author=author)
    return render(request,'Authors/author_detail.html',{"author":author,"books":books})



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