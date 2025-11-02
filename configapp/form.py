from django import forms
from .models import Category, Product, Supplier, Order, Customer
from datetime import date
import re

class CategoryForm(forms.Form):
    title = forms.CharField(max_length=100, label="Category Title")

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title[0].isupper():
            raise forms.ValidationError("Title 1-chi harfi katta bolishi kerak.")
        if any(ch.isdigit() for ch in title):
            raise forms.ValidationError("Title ichida raqam bolmasin.")
        return title

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Product Name")
    price = forms.FloatField(label="Price")
    category = forms.ChoiceField(label="Category")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        self.fields['category'].choices = [(cat.id, cat.title) for cat in categories]

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise forms.ValidationError("Nomda raqam yoki tinish belgisi bolmasin.")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if not (1 < price < 10):
            raise forms.ValidationError("Narx 1 dan katta va 10 dan kichik bolishi kerak.")
        return price

class SupplierForm(forms.Form):
    name = forms.CharField(max_length=100, label="Supplier Name")
    city = forms.CharField(max_length=50, label="City")
    region = forms.CharField(max_length=50, label="Region")

    def clean_city(self):
        city = self.cleaned_data['city']
        if not city[0].isupper():
            raise forms.ValidationError("Shahar nomi bosh harfi katta bolishi kerak.")
        return city

    def clean_region(self):
        region = self.cleaned_data['region']
        if not region[0].isupper():
            raise forms.ValidationError("Region nomi bosh harfi katta bolishi kerak.")
        return region

class OrderForm(forms.Form):
    order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Order Date")
    product = forms.ChoiceField(label="Product")
    supplier = forms.ChoiceField(label="Supplier")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = Product.objects.all()
        suppliers = Supplier.objects.all()
        self.fields['product'].choices = [(p.id, p.name) for p in products]
        self.fields['supplier'].choices = [(s.id, s.name) for s in suppliers]

    def clean_order_date(self):
        order_date = self.cleaned_data['order_date']
        if order_date < date(2025, 1, 1):
            raise forms.ValidationError("Order sanasi 2025-01-01 dan katta bolishi kerak.")
        return order_date

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100, label="Customer Name")
    email = forms.EmailField(label="Email")
