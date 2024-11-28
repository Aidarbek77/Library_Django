from . import views
from django.urls import path, include


urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('orders/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete_order'),
    path('orders/<int:id>/update/', views.UpdateOrderView.as_view(), name='update_order'),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),

]