from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Book

def first_lesson_django(request):
    if request.method == 'GET':
        return HttpResponse('🐍Hello DJANGO TEMPLATES 🐍')

def picture_view(request):
    if request.method == 'GET':
        return HttpResponse("<img src = 'https://itproger.com/img/news/1592990176.jpg'  >")

def about_me(request):
    info = "Меня зовут Айдар, я ученик группы46-1B."
    return HttpResponse(info)

def about_my_pets(request):
    pet_name = "Барсик"
    pet_photo_url = "/templates/pet1.jpg"
    return render(request, 'about_my_pets.html', {'pet_name':pet_name, 'pet_photo_url': pet_photo_url})

def system_time(request):
    current_time = datetime.now()
    return HttpResponse(f"Системная дата и время: {current_time}")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})
