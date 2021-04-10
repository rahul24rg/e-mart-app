from django.contrib import admin
from .models.product import Product
from .models.catrogry import Cateogrie
from .models.customer import Customer

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'cateogry']

class CateogryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(Product, AdminProduct)
admin.site.register(Cateogrie,CateogryAdmin)
admin.site.register(Customer,CustomerAdmin)
