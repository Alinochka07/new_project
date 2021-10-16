from django.urls import path
from .views import *
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('', product_list, name='product-list'),
    path('<int:id>/<product_slug>/', views.product_detail, name='product-detail'),
    path('<category_slug>/', views.product_list, name='category-list'),
    path('delivery', DeliveryPage.as_view(), name='delivery'),
    path('search/', ProductListView.as_view, name='search'),
    path('addcomment/<int:id>/', views.addcomment, name='addcomment'),
    # path('/search/', views.searchbar, name='search'),
]