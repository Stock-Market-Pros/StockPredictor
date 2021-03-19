from rest_framework import serializers
from home.models import Stock

class StockSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stock
    fields = '__all__'