from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddGoodForm


@require_POST
def add_to_cart(request, good_id):
    cart = Cart(request)  
    good = get_object_or_404(Good, id=good_id) 
    form = CartAddGoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(good=good, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def remove_from_cart(request, good_id):
    cart = Cart(request)
    product = get_object_or_404(Good, id=good_id)
    cart.remove(good)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for shopitem in cart:
        shopitem['update_quantity_form'] = CartAddGoodForm(initial={'quantity': shopitem['quantity'], 'update': True})
    return render(request, 'cart/cartdetail.html', {'cart': cart})