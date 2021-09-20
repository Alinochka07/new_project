from django.db import models
from django.contrib import admin 
from django.contrib.auth.models import User
from django.urls import reverse 
from django.utils import timezone



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



class Good(models.Model):
    
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название товара")
    category = models.ForeignKey(Category, related_name='товары', verbose_name="Категория",on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media', blank=True, verbose_name="Картинка")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.IntegerField(default=0, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Количество в наличии")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    # sale = models.IntegerField(default=0, verbose_name="Скидка %")

    # def get_sale(self):
    #     price = int(self.price * (100 - self.sale) / 100)
    #     return price

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
        return reverse('mainapp:goods-detail', args=[self.id, self.slug])