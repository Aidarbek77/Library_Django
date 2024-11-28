from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from django.views import generic
from django.shortcuts import get_object_or_404


class OrderListView(generic.ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'orders'
    model = Order

    def get_queryset(self):
        return Order.objects.all()


class CreateOrderView(generic.CreateView):
    form_class = OrderForm
    template_name = 'order/create_order.html'
    success_url = '/backet/orders/'

    def form_valid(self, form):
        return super(CreateOrderView, self).form_valid(form)


class DeleteOrderView(generic.DeleteView):
    template_name = 'order/delete_order.html'
    success_url = '/backet/orders/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)

    def form_valid(self, form):
        return super(DeleteOrderView, self).form_valid(form)


class UpdateOrderView(generic.UpdateView):
    form_class = OrderForm
    template_name = 'order/update_order.html'
    success_url = '/backet/orders/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)

    def form_valid(self, form):
        return super(UpdateOrderView, self).form_valid(form)


class OrderDetailView(generic.DetailView):
    template_name = 'order/order_detail.html'
    context_object_name = 'order'
    model = Order

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)