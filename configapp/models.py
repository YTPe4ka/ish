from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import re

class Category(models.Model):
    title = models.CharField(max_length=100)

    def clean(self):
        if not self.title[0].isupper() is None:
            raise ValidationError("title 1-chi harfi katta bolishi kerak.")
        if any(ch.isdigit() for ch in self.title):
            raise ValidationError("title ichida raqam bolmasin.")

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def clean(self):
        if not re.match(r'^[A-Za-z\s]+$', self.name):
            raise ValidationError("nomda raqam yoki tinish belgisi bolmasin.")
        if not (1 < self.price < 10):
            raise ValidationError("narx 1 dan katta va 10 dan kichik bolishi kerak.")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def clean(self):
        if not self.city[0].isupper():
            raise ValidationError("shahar nomi bosh harfi katta bolishi kerak.")
        if not self.region[0].isupper():
            raise ValidationError("region nomi bosh harfi katta bolishi kerak.")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField() 
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def clean(self):
        if self.order_date is None:
            raise ValidationError("Order date is required.")

        if self.order_date < date(2025, 1, 1):
            raise ValidationError("Order date must be 2025-01-01 or later.")

    def __str__(self) :
        return f"Order {self.product.name} - {self.order_date}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
