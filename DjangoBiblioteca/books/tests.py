from django.test import TestCase
from .models import Author, Book, Genre

# Create your tests here.

class AuthorTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Smith', birth_date="1928-12-31")

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, 'John')
        self.assertEqual(self.author.last_name, 'Smith')
        self.assertEqual(self.author.birth_date, '1928-12-31')

class GenreTests(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Misterio')

    def test_genre_creation(self):
        self.assertEqual(self.genre.name, 'Misterio')

class BookTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Smith', birth_date="1928-12-31")
        self.genre = Genre.objects.create(name='Misterio')
        self.book = Book.objects.create(
            title='The Book',
            genre=self.genre,
            publish_date="2010-01-01",
            summary="Test libro"
        )
        self.book.author.add(self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'The Book')
        self.assertEqual(self.book.author, 'John')
        self.assertEqual(self.book.genre.name, "Misterio")
        self.assertEqual(self.book.publish_date, "2010-01-01")
        self.assertEqual(self.book.summary, "Test libro")