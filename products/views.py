from django.shortcuts import render
from . models import Product
from category.models import Category
# Create your views here.
def productlist(request):
    products = Product.objects.all().filter(availability=True)
    product_count = products.count()
    categories = Category.objects.all()
    context = {
        'products': products,
        'count': product_count,
        'categories': categories
    }
    return render(request,'products/product-list.html',context=context)