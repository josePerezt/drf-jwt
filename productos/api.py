from rest_framework import viewsets,permissions 
from .serializers import ProducSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProducSerializer
  permission_classes = [permissions.AllowAny]