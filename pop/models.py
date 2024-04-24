# models.py for the 'pop' app

from django.db import models
from django.contrib.auth.models import User
from inv.models import Product

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.supplier_name

class PurchaseOrder(models.Model):
    purchase_order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Purchase Order {self.purchase_order_id}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product.product_name} ({self.quantity_ordered} units)"
