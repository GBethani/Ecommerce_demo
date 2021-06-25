from django.urls import path
from .views import productlist, product_detail

app_name = 'products'

urlpatterns = [
    path('',productlist,name='product-list'),
    path('<slug:category_slug>/',productlist,name='products-by-category'),
    path('<slug:category_slug>/<slug:product_slug>/',product_detail,name='product-detail'),
]
