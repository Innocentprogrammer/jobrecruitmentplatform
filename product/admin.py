from django.contrib import admin
from product.models import Product 

class productAdmin(admin.ModelAdmin):
    list_display = ('product_image','product_name','product_desc')

admin.site.register(Product,productAdmin)
# Register your models here.
