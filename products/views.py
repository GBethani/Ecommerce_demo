from django.shortcuts import render, get_object_or_404
from . models import Product
from category.models import Category
# Create your views here.
def productlist(request,category_slug=None):
    # category = None
    # products = None
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.all().filter(category=category,availability=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(availability=True)
        product_count = products.count()
    context = {
        'products': products,
        'count': product_count,
    }
    return render(request,'products/product-list.html',context=context)