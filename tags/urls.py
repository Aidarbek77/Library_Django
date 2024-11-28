from django.urls import path, include
from . import views

urlpatterns = [
    path('older/', views.OlderListView.as_view(), name='older'),
    path('younger/', views.YoungerListView.as_view(), name='younger'),
    path('kids/', views.KidsListView.as_view(), name='kids'),
    path('all/', views.AllListView.as_view(), name='all'),
]