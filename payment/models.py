import uuid

from django.db import models

from order.models import Order


# Create your models here.
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.order.name} - {self.price}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
