from django.test import TestCase
from inventory.models import Product, Category,Inventory,Order,OrderLine
from inventory.serializers import ProductSerializer,CategorySerializer,InventorySerializer,OrderSerializer,OrderLineSerializer
from django.contrib.auth import get_user_model
import datetime


#This test code:
#  - Checks the presence of all fields
#  - Verifies the correctness of the serialized data

User = get_user_model()

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(category_name='Test Product',user=self.user)
        self.product = Product.objects.create(
            product_name= 'Test Product',
            product_code= 12345,
            weight= 1.5,
            color= 'Red',
            dimensions= '10*20*30',
            brand= 'usa',
            country_of_manufacture= 'usa',
            expiration_date= datetime.date(2025, 7, 12),
            category= self.category,
            user= self.user
        )
        
    def test_product_serializer_contains_expected_fields(self):
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        self.assertEqual(set(data.keys()), {
            'id','product_name','product_code','weight','color',
            'dimensions','country_of_manufacture','brand','expiration_date',
            'user','category'
        })
    
    def test_product_serializer_data_content(self):
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        self.assertEqual(data['product_name'], 'Test Product')
        self.assertEqual(data['product_code'], 12345)
        self.assertEqual(data['weight'], 1.5)
        self.assertEqual(data['color'], 'Red')
        self.assertEqual(data['dimensions'], '10*20*30')
        self.assertEqual(data['country_of_manufacture'], 'usa')
        self.assertEqual(data['brand'], 'usa')
        self.assertEqual(data['expiration_date'], '2025-07-12')
        self.assertEqual(data['user'], 'testuser')
        self.assertEqual(data['category'], self.category.id)        
