from django.urls import path
from . import views

urlpatterns = [
    path('',views.books,name='Books'),
    path('book/<int:pk>/',views.BookDetail.as_view(),name='book_detail'),
    path('book/<pk>/delete/',views.BookDelete.as_view(),name='book_delete'),
    path('book/<int:pk>/edit/',views.BookUpdate.as_view(),name='book_update'),
    path('book/new/',views.BookCreate.as_view(),name='book_new'),
]