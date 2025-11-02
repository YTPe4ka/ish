from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),

    path('add_category/', views.add_category, name='add_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),

    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('delete-supplier/<int:id>/', views.delete_supplier, name='delete_supplier'),

    path('add-order/', views.add_order, name='add_order'),
    path('delete-order/<int:id>/', views.delete_order, name='delete_order'),

    path('add-customer/', views.add_customer, name='add_customer'),
    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),
]
