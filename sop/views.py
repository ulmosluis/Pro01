# views.py for the 'sop' app
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Customer, SalesOrder, OrderItem

class CustomerListView(ListView):
    model = Customer
    template_name = 'sop/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'sop/customer_detail.html'
    context_object_name = 'customer'

class SalesOrderListView(ListView):
    model = SalesOrder
    template_name = 'sop/salesorder_list.html'
    context_object_name = 'salesorders'

class SalesOrderDetailView(DetailView):
    model = SalesOrder
    template_name = 'sop/salesorder_detail.html'
    context_object_name = 'salesorder'

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'sop/orderitem_list.html'
    context_object_name = 'orderitems'

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'sop/orderitem_detail.html'
    context_object_name = 'orderitem'