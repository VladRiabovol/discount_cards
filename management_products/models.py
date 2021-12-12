from django.db import models
from management_discount_cards.models import Card


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(default=0.0, max_digits=12, decimal_places=2)


class Purchase(models.Model):
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                blank=True, null=True, default=None)
    number = models.IntegerField(default=0)
    price_per_item = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.title} {self.product.price}'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_amount = int(self.number) * price_per_item
        super(Purchase, self).save(*args, **kwargs)
