from .models import Order, OrderItem
from products.models import Product
from products.ProductSerializer import ProductSerializer
from rest_framework import serializers
from django.db.models import JSONField


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product.id')

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):

    # queryset = OrderItem.objects.all()
    # products = ProductSerializer(source="Product", many=True, read_only=True)
    products = serializers.SerializerMethodField() 

    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_amount', 'status', 'delivery_status', 'products']

    def get_products(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data
