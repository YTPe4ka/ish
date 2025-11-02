from django.shortcuts import render, redirect
from .form import CategoryForm, ProductForm, SupplierForm, OrderForm, CustomerForm
from .models import Product, Category, Supplier, Order, Customer
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'product_list.html', {'products': products, 'orders': orders})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data['title']
            )
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'category koshish'})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(id=form.cleaned_data['category'])
            Product.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                category=category
            )
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'product koshish'})

def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            Supplier.objects.create(
                name=form.cleaned_data['name'],
                city=form.cleaned_data['city'],
                region=form.cleaned_data['region']
            )
            return redirect('home')
    else:
        form = SupplierForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'sotuvchini koshish'})

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=form.cleaned_data['product'])
            supplier = Supplier.objects.get(id=form.cleaned_data['supplier'])
            Order.objects.create(
                order_date=form.cleaned_data['order_date'],
                product=product,
                supplier=supplier
            )
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'zakaz koshish'})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'form_page.html', {'form': form, 'title': 'klient koshish'})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('home')

def delete_supplier(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    supplier.delete()
    return redirect('home')

def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('product_list')

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('home')





