from django.db import models


class Card(models.Model):
    series = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    end_of_activity = models.DateField()
    date_of_use = models.DateTimeField(auto_now=True)
    total_sum = models.DecimalField(default=0.0, max_digits=12, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id}, number: {self.number}'

