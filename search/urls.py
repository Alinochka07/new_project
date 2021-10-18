from django.urls import path
from .views import *
from . import views


app_name = 'search'
urlpatterns = [
    path('', views.search, name='product_search'),
    # path('search/', views.product_search, name='product_search'),
    # path('search/', views.search, name='search'),
]