from django.contrib import admin
from django.utils.html import format_html
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} width="40" height="40"/>'.format(object.category_image.url))
    thumbnail.short_description = 'Pic'
    
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','thumbnail','slug']
    list_filter = ['date_created','date_modified']
    search_fields = ['name',]

admin.site.register(Category,CategoryAdmin)