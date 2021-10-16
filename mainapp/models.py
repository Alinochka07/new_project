from django.db import models
from django.contrib import admin 
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone
from django.db.models import Q
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:category-list', args=[self.slug])



class Product(models.Model):
    
    name = models.CharField(max_length=200, verbose_name="Название товара")
    category = models.ForeignKey(Category, verbose_name="Категория",on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media', blank=True, verbose_name="Картинка")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.IntegerField(default=0, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Количество в наличии")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    
    def averagereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(average=Avg('rate'))
        avg=0
        if reviews["average"] is not None:
            avg=float(reviews["average"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product-detail', args=[self.id, self.slug])



 
class ProductManager(models.Manager):
    use_for_related_fields = True
 
    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(name__icontains=query))
            qs = qs.filter(or_lookup)
 
        return qs


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

