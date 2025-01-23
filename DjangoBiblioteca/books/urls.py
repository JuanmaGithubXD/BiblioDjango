from django.urls import path

from books import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path("book/<int:book_id>", views.book_detail, name='detalles_libro'),
    path("authors/",views.author_list, name='lista_autor'),
    path("author/<int:author_id>", views.author_detail, name='detalles_autor'),
    path("genres/", views.genre_list, name='lista_genero'),
    path("genre/<int:genre_id>", views.genre_detail, name='detalles_genero'),
]