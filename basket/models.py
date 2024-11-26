from django.db import models
from books.models import Book

class Order(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
