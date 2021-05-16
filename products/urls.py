from django.urls import path
from .views import productlist

app_name = 'products'

urlpatterns = [
    path('',productlist,name='product-list'),
]
