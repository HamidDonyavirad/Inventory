from rest_framework import serializers
from .models import Product,Category, Inventory, Order,OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        user= User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
        
        
        
class ProductSerializer(serializers.ModelSerializer):
    color = serializers.CharField(required=False,allow_blank=True)
    dimensions = serializers.CharField(required=False,allow_blank=True)
    brand = serializers.CharField(required=False,allow_blank=True)
    class Meta:
        model = Product
        fields = ['id','product_name','product_code','weight','color','dimensions','country_of_manufacture','brand','expiration_date','user','category']
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name','user']

        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id','transaction_type','quantity','date','user','product']    
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order_number','transaction_type','costomer_or_supplier_choices','date','status',]                            
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields =['id','price','quantity','order','product']            
        