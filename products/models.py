from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images/products/%Y/%m/%d/',blank=True,null=True)
    availability = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('products:product-detail',args=[self.category.slug,self.slug])

    @property
    def dollar_amount(self):
        return '$%s' % self.price if self.price else "" 
    
