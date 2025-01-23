from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    publish_date = models.DateField()
    summary = models.TextField()
    def __str__(self):
        return f"{self.title}"



