from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('first_name','last_name','username','email','last_login',)
    list_filter = ('date_joined','is_staff')
    readonly_fields = ('date_joined','last_login',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    fieldsets = ()  # keeps the password read only
    
admin.site.register(Account,AccountAdmin)
