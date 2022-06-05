from django.contrib import admin
from django.urls import path
from products.views import productList,UserProductList,ProductListCreate,UserProductUpdateDelete,UserProductBid,UserProductBought

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', productList.as_view()),
    path('my_products/', UserProductList.as_view()),
    path('Add/', ProductListCreate.as_view()),
    path('my_products/<int:pk>/', UserProductUpdateDelete.as_view()),
    path('my_products/successful_bids/', UserProductBought.as_view()),
    path('products/bids/<int:pk>', UserProductBid.as_view())
]

