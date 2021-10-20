from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import View, ListView
from .models import *
from cart.forms import CartAddProductForm
from django.db.models import Q





# Страница с товарами
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'product/mainlist.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

# Страница товара
def product_detail(request, id, product_slug):
    query = request.GET.get('q')
    product = get_object_or_404(Product, id=id, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm()
    comments = Comment.objects.filter(product_id=id,status='True')
    
    return render(request, 'product/productdetail.html', {
        'product': product, 
        'cart_product_form': cart_product_form,
        'comments': comments})



# Страница по доставке
class DeliveryPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'delivery.html')



# Отзывы
def addcomment(request,id):
   url = request.META.get('HTTP_REFERER') 
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment() 
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.product_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save() 
         messages.success(request, "Ваш отзыв успешно отправлен модератору сайта. Благодарим Вас!")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)



class ContactUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact_us.html')



 
