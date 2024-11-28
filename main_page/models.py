from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              related_name='books')
    author_gmail = models.EmailField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE,
                             related_name='comments')

    def __str__(self):
        return self.text