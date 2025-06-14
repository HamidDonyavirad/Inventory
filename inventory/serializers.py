from rest_framework import serializers
from .models import Product,Category, Inventory, Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name','product_code','weight','color','dimensions','country_of_manufacture','brand','expiration_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']

        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','transaction_type','quantity','date']    
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','order_number','transaction_type','costomer_or_supplier_choices','date','status',]                            
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','price','quantity']            
        