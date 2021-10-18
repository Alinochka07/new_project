from django.shortcuts import render
from mainapp.models import *
from mainapp.views import *
from .forms import *

# Поиск
# def product_search(request):
#     if request.method == 'POST':
#         search_term = request.POST.get('name')
#         if search_term:
#             results = Product.objects.filter(name__icontains=search_term)
#             return render(request, 'search_products.html', {'results': results})
#     return render(request, 'search_products.html')

def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] 
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(name__icontains=query)
            else:
                products = Product.objects.filter(name__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')