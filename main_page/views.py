from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from books.views import book_list
from . import models
from django.views import generic

class BookListView(generic.ListView):
    template_name = 'show.html'
    context_object_name = 'film_list'
    model = models.Books

    def get_queryset(self):
        return models.Books.objects.filter().order_by('-id')

#serch button
class SearchView(generic.ListView):
    template_name = 'show.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class BookDetailView(generic.DetailView):
    template_name = 'show_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)





def first_lesson_django(request):
    if request.method == 'GET':
        return HttpResponse('🐍Hello DJANGO TEMPLATES 🐍')

def picture_view(request):
    if request.method == 'GET':
        return HttpResponse("<img src = 'pet.jpg'  >")

def about_me(request):
    info = "Меня зовут Айдар, я ученик группы46-1B."
    return HttpResponse(info)

def about_my_pets(request):
    pet_name = "Барсик"
    pet_photo_url = "/templates/pet.jpg"
    return render(request, 'about_my_pets.html', {'pet_name':pet_name, 'pet_photo_url': pet_photo_url})

def system_time(request):
    current_time = datetime.now()
    return HttpResponse(f"Системная дата и время: {current_time}")

def book_list(request):
    books = book_list().objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(book_list(), pk=pk)
    return render(request, 'book_detail.html', {'book': book})

