# views.py for the 'pop' app
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Supplier, PurchaseOrder, PurchaseOrderItem

class SupplierListView(ListView):
    model = Supplier
    template_name = 'pop/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'pop/supplier_detail.html'
    context_object_name = 'supplier'

class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'pop/purchaseorder_list.html'
    context_object_name = 'purchaseorders'

class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder
    template_name = 'pop/purchaseorder_detail.html'
    context_object_name = 'purchaseorder'

class PurchaseOrderItemListView(ListView):
    model = PurchaseOrderItem
    template_name = 'pop/purchaseorderitem_list.html'
    context_object_name = 'purchaseorderitems'

class PurchaseOrderItemDetailView(DetailView):
    model = PurchaseOrderItem
    template_name = 'pop/purchaseorderitem_detail.html'
    context_object_name = 'purchaseorderitem'
