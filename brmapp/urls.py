from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path("", views.helloView, name="store"),
    path("add-book/",views.addBookView, name="add-book"),
    path("addbook-data/",views.addBook, name="addition"),
    path("edit-book/<book_id>",views.editBookView, name="edit-book"),
    path("edit-book/edit/<book_id>",views.editBook, name="edition"),
    path("delete/<book_id>",views.deleteBook, name="delete-book"),
 
]