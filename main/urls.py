from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from main_page import views
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
    path('system_time/', views.system_time, name='system_time'),
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('admin/', admin.site.urls),
    path('library/', include('your_app_name.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)
