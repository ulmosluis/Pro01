from django.db import models
from django.contrib.auth.models import User
from inv.models import Product

# Create your models here.
# models.py for the 'sop' app

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name

class SalesOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.order_id}"

class OrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    createdDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.product_name} ({self.quantity_ordered} units)"

