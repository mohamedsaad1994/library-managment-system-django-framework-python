from django.urls import path
from . import views

urlpatterns = [
    path('',views.authors,name='Authors'),
    path('author/<int:pk>/',views.AuthorDetail.as_view(),name='author_detail'),
    path('author/<pk>/delete/',views.AuthorDelete.as_view(),name='author_delete'),
    path('author/<int:pk>/edit/',views.AuthorUpdate.as_view(),name='author_update'),
    path('author/new/',views.AuthorCreate.as_view(),name='author_new'),
    
]