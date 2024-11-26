from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Books(models.Model):
    GENRE_CHOICE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Боевик', 'Боевик')
    )
    image = models.ImageField(upload_to='book/', verbose_name='загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Укажите описание книги')
    description = models.TextField(verbose_name='Укажите описание к ', default='Lorem Ipsum', null=True)
    price = models.FloatField(verbose_name='Укажите цену')
    start_film = models.DateField(verbose_name='укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Комедия',
                             verbose_name='Укажите жанр')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def average_rating(self):
        reviews  = self.review_books.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    class Meta:
        verbose_name = 'книги'
        verbose_name_plural = 'книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'


class ReviewBook(models.Model):
    review_films = models.ForeignKey(Books, on_delete=models.CASCADE,
                                     related_name='review_books')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзыв о книге')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_films}-{self.created_at}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'