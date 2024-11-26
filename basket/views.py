from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'basket/order_list.html', {"orders": orders})

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'basket/order_form.html', {"form": form})
