from django.shortcuts import render

# Create your views here.
from .models import Book, Genre, Author

#Pagina principal
def index(request):
    books = Book.objects.all()
    return render(request,"index.html",context={"books":books})

#Detalles del libro
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "detalles_libro.html", context={"book":book})

#Lista de generos
def genre_list(request):
    genres = Genre.objects.all()
    return render(request,"lista_genero.html",context={"genres":genres})

#Detalles genero
def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, "detalles_genero.html", context={"genre":genre})

#Lista de autores
def author_list(request):
    authors = Author.objects.all()
    return render(request,"lista_autor.html",context={"authors":authors})

#Detalles de autor
def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "detalles_autor.html", context={"author":author})




