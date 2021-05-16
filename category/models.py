from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField(blank=True,null=True)
    category_image = models.ImageField(upload_to='images/categories/%Y/%m/%d/',blank=True,null=True)
    # auto_now = last modified; auto_now_add = created
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('products:products-by-category',args=[self.slug])
