from rest_framework import serializers
from .models import product , Product_Category

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"
    
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"
