from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.user.name} - {self.product.name}'

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True)
    stage = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name} : Order - {self.number}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.order.name} - {self.product.name}'

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'
