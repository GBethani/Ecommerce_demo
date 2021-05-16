from django.contrib import admin
from django.utils.html import format_html
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} width="40" height="40"/>'.format(object.image.url))
    thumbnail.short_description = 'Pic'

    list_display = ('category','product_name','thumbnail','dollar_amount','stock','availability')
    prepopulated_fields = {'slug':('product_name',)}
    list_filter = ('stock',)

admin.site.register(Product,ProductAdmin)