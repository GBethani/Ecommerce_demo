from django.shortcuts import render
from products.models import Product

def home(request):
    products = Product.objects.all().filter(availability=True)
    context = {
        'products': products,
    }
    return render(request,'index.html',context=context)