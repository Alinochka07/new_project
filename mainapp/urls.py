from django.urls import path, re_path
from .views import *
from . import views


app_name = 'mainapp'
urlpatterns = [
    re_path('', goods_list, name='goods-list'),
    re_path('<int:id>/<good_slug>/', goods_detail, name='goods-detail'),
    re_path('<category_slug>/', goods_list, name='category-list'),
]