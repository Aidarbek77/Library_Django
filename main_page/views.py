from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.views import generic
from . import models
from .forms import CommentForm


def about_me(request):
    return render(request, 'main_page/about_me.html')


def about_my_pet(request):
    return HttpResponse(f"Its my cat - MURZIK")


def current_tima(request):
    return HttpResponse(datetime.datetime.now())


class BookListView(generic.ListView):
    template_name = 'main_page/book.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'main_page/book_detail.html'
    model = models.Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.object
            comment.save()
            return redirect('book-detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)