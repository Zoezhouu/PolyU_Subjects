from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    quantity = models.PositiveIntegerField()
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )

    DELIVERY_STATUS_CHOICES = (
        ('not_delivered', 'Not Delivered'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='not_delivered')

    def __str__(self):
        return f"Order by {self.customer.username} - Status: {self.status}, Delivery Status: {self.delivery_status}"
