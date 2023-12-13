from rest_framework import viewsets
from .models import Product
from .ProductSerializer import ProductSerializer
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
