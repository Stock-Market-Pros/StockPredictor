from home.models import Stock
from rest_framework import viewsets, permissions
from .serializers import StockSerializer

#Stock Viewset
class StockViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = StockSerializer