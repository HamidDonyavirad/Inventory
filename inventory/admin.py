from django.contrib import admin
from .models import Product,Category,Inventory,Order, OrderItem   
# Register your models here.

admin.site.register(Product)