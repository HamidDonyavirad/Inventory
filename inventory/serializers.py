from rest_framework import serializers
from .models import Product,Category, Inventory, Order,OrderLine
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
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
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
        fields = ['id','transaction_type','unit_type','quantity','date','user','product'] 
    
    def validate(self, data):
        transaction_type = data.get('transaction_type')
        quantity = data.get('quantity')
        date = data.get('date') 
        product_id = data.get('product')
        if transaction_type == Inventory.OUTBOUND: 
            inventories = Inventory.objects.filter(product=product_id).order_by('date')
            current_stock = 0
            for inv in inventories:
                if inv.transaction_type == Inventory.INBOUND:
                    current_stock += inv.quantity
                elif inv.transaction_type == Inventory.OUTBOUND:
                    current_stock -= inv.quantity 
                    
            if quantity > current_stock:
                raise serializers.ValidationError(
                    {'quantity':'There is not enough balance for this transfer'}
                ) 
                
        return data                       
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order_number','transaction_type','role','role_name','date','status',]                            
        
        
class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields =['id','price','quantity','order','product']            
        