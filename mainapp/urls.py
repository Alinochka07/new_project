from django.urls import path
from .views import *
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('', views.goods_list, name='goods-list'),
    path('<int:id>/<good_slug>/', views.goods_detail, name='goods-detail'),
    path('<category_slug>/', views.goods_list, name='category-list'),
]