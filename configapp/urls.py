from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('add-order/', views.add_order, name='add_order'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('products/', views.product_list, name='product_list'),

]
