# views.py for the 'inv' app
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product, Location, Stock

class CategoryListView(ListView):
    model = Category
    template_name = 'inv/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'inv/category_detail.html'
    context_object_name = 'category'

class ProductListView(ListView):
    model = Product
    template_name = 'inv/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'inv/product_detail.html'
    context_object_name = 'product'

class LocationListView(ListView):
    model = Location
    template_name = 'inv/location_list.html'
    context_object_name = 'locations'

class LocationDetailView(DetailView):
    model = Location
    template_name = 'inv/location_detail.html'
    context_object_name = 'location'

class StockListView(ListView):
    model = Stock
    template_name = 'inv/stock_list.html'
    context_object_name = 'stocks'

class StockDetailView(DetailView):
    model = Stock
    template_name = 'inv/stock_detail.html'
    context_object_name = 'stock'

