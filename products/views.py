from rest_framework import generics , permissions , status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Category, ActiveBids
from .serializers import productSerializer, categorySerializer, activeBidsSerializer
import datetime
class productList(generics.ListAPiView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permissions = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        category = request.query_params.get("category", None)
        name = request.query_params.get("Name", None)
        if category is not None:
            self.queryset = self.queryset.filter(category__Name=category)
        if name is not None:
            self.queryset = self.queryset.filter(Name=name)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

class UserProductList(generics.ListAPiView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permissions = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permissions = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permissions = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



class UserProductBid(APIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permissions = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.all()
    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        product = Product.objects.get(id=product_id)
        product.Bid_Current_price = request.data.get("Bid_Current_price")
        self.save()
        product.save()
        product.last_bid_time = Product.objects.filter(product=self).latest('time').time
        product.save()
        return Response(status=status.HTTP_200_OK)
    def check_status(self):
        if self.last_bid_time + datetime.timedelta(hours=24) < datetime.datetime.now():
            self.status = 'S'
            Product.sold_to = Product.objects.filter(product=self).latest('time').user
            Product.save()
            self.save()
        else:
            self.status = 'A'
            self.save()
   

class UserProductBought(generics.ListAPiView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permissions = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(sold_to=self.request.user)

