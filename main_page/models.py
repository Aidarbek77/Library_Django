from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_date = models.DateField()
    page_count = models.IntegerField()
    cover_url = models.URLField()
    language = models.CharField(max_length=2)

    def __str__(self):
        return self.title