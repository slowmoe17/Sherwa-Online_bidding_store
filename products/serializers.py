from rest_framework import serializers
from .models import Product, Category, ActiveBids

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class activeBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveBids
        fields = "__all__"