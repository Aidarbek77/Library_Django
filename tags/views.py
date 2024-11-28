from django.shortcuts import render
from .models import Tag, Cloth
from django.views import generic


class OlderListView(generic.ListView):
    template_name = 'tags/older.html'
    context_object_name = 'older'
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='For Olds')


class YoungerListView(generic.ListView):
    template_name = 'tags/younger.html'
    context_object_name = 'younger'
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='For Young')


class KidsListView(generic.ListView):
    template_name = 'tags/kids.html'
    context_object_name = 'kids'
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='For Kids')


class AllListView(generic.ListView):
    template_name = 'tags/all.html'
    context_object_name = 'alls'
    model = Cloth

    def get_queryset(self):
        return Cloth.objects.all()