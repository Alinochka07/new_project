from django.db import models

from mainapp.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=60, verbose_name='Ваше имя')
    last_name = models.CharField(max_length=60, verbose_name='Фамилия')
    email = models.EmailField()
    DELIVER = 'Доставка'
    NO_DELIVER = 'Самовывоз'
    DELIVERY = [(DELIVER, 'Доставка'), (NO_DELIVER, 'Самовывоз')]
    deliveries = models.CharField(max_length=10, choices=DELIVERY, verbose_name='Опция доставки')
    address = models.CharField(max_length=150, verbose_name='Адрес доставки')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    comments = models.CharField(max_length=200, verbose_name='Комментарии к заказу')

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.shopitems.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='shopitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

