from django.contrib import admin
from .models import Book, Genre, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'created_at', 'genre', 'author_gmail', 'author')
    list_filter = ('created_at', 'genre',)
    search_fields = ('title', 'description', 'author', 'author_gmail')


admin.site.register(Genre)
admin.site.register(Comment)