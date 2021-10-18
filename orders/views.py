from django.shortcuts import render
from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from account.models import *
from account.views import *


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for shopitem in cart:
                OrderItem.objects.create(
                    order=order,
                    product=shopitem['product'],
                    price=shopitem['price'],
                    quantity=shopitem['quantity']
                )
            cart.clear()
        return render(request, 'order/orders.html', {'order': order})
    else:
        form = CreateOrderForm()
    return render(request, 'order/createorder.html', {'form': form})

