# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User
from products.models import Product


# Create your models here.
class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[
            MinValueValidator(1)
        ])
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_purchase = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{User: self.user.name} Product: {self.product.name} Date: {self.date_of_purchase}'

class Rate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    score = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return f'User: {self.user.name} Product: {self.product.name} Rating: {self.score}'