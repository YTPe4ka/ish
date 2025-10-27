from django.shortcuts import render, redirect
from .form import CategoryForm, ProductForm, SupplierForm, OrderForm, CustomerForm

def home(request):
    return render(request, 'home.html')

def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form_page.html', {'form': form, 'title': 'category koshish'})

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form_page.html', {'form': form, 'title': 'product koshish'})

def add_supplier(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form_page.html', {'form': form, 'title': 'sotuvchini koshish'})

def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form_page.html', {'form': form, 'title': 'zakaz koshish'})

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form_page.html', {'form': form, 'title': 'klient koshish'})
