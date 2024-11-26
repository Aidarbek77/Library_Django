from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    hashtag = models.CharField(max_length=50, choices=[("old", "Старики"), ("young", "Молодежь"), ("children", "Дети")])
    stock = models.PositiveIntegerField(default=0)
