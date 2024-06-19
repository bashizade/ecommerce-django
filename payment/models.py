from django.db import models

from order.models import Order
from main.models import MainModel


# Create your models here.
class Payment(MainModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.order.name} - {self.price}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
