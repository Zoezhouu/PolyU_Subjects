from rest_framework import viewsets
from .models import Order, OrderItem
from products.models import Product
from .OrderSerializer import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from django.db import transaction


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # check if serializer is valid
        # self.perform_create(serializer)
        # Wrap the entire process in a database transaction
        with transaction.atomic():
            try:
                products = request.data.get("products")
                if not products or len(products) == 0:
                    return Response({"error": "You must provide products."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    for product in products:
                        if not product.get("product_id") or not product.get("quantity"):
                            return Response({"error": "You must provide product_id and quantity for each product."}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            product_id = product.get("product_id")
                            quantity = product.get("quantity")
                            product_obj = Product.objects.get(id=product_id)
                            if product_obj.stock < quantity:
                                return Response({"error": f"Product {product_obj.name} does not have enough stock."}, status=status.HTTP_400_BAD_REQUEST)
                            else:
                                product_obj.stock -= quantity
                                product_obj.save()
                                # add to order item table
                                order_item = OrderItem(order=serializer.save(), product=product_obj, quantity=quantity)
                                order_item.save()
            except Exception as e:
                # If an error occurs, rollback the transaction
                transaction.set_rollback(True)
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # return response with 201 status code

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer