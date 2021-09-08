from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import DetailView, View, TemplateView
from .models import Category, Good
from django.views import View
from cart.forms import CartAddGoodForm



# Страница с товарами
def goods_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    goods = Good.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        goods = goods.filter(category=category)
    
    return render(request, 'good/mainlist.html', {
        'category': category,
        'categories': categories,
        'goods': goods
    })

# Страница товара
def goods_detail(request, id, good_slug):
    good = get_object_or_404(Good, id=id, slug=good_slug, available=True)
    cart_good_form = CartAddGoodForm()
    return render(request, 'good/gooddetail.html', {
        'good': good, 
        'cart_good_form': cart_good_form})
