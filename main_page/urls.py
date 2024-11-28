from django.urls import path, include
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('about_my_pet/', views.about_my_pet),
    path('current_time/', views.current_tima),
    path('book/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]