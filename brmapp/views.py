from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def helloView(request):
    books = Book.objects.all()
    return render(request, "seebook.html", {"books": books})


def addBookView(request):
    
     return render(request, "addbook.html")

def addBook(request):
    if request.method== "POST":
        try:        
            book = Book()
            book.title = request.POST["title"]
            book.price = request.POST["price"]
            book.save()
            return HttpResponseRedirect("/")
        except ValueError:
            error_message = "Price must be a number!"
            return render(request, "addbook.html", {"error_message": error_message})



def editBookView(request, book_id):
    book=Book.objects.get(id=book_id)
    print(book)
    return render (request, "editbook.html", {"book":book})



def editBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
            try:
            # Update book instance with data from the request
                book.title = request.POST.get("title")
                book.price = request.POST.get("price")
                book.save()
                return HttpResponseRedirect("/")  # Redirect to home or appropriate URL
            
            except ValueError:
                err_message = "Price must be a number!"
                return render(request, "editbook.html", {"err_message": err_message, "book":book})



def deleteBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)           
    book.delete()
    return HttpResponseRedirect("/")  # Redirect to home or appropriate URL

