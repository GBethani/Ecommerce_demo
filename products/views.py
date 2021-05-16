from django.shortcuts import render
from . models import Product
# Create your views here.
def productlist(request):
    products = Product.objects.all().filter(availability=True)
    product_count = products.count()
    context = {
        'products': products,
        'count': product_count
    }
    return render(request,'products/product-list.html',context=context)