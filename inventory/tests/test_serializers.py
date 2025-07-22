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
            user= self.user,
            category= self.category,
            
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

class CategorySerializersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(category_name='Test Product',user=self.user)
    
    
    def test_category_seializer_contains_expected_fields(self):
        serializer = CategorySerializer(instance = self.category) 
        data = serializer.data   
        self.assertEqual(set(data.keys()),{
            'id','category_name','user'
        }) 
    
    def test_category_seializer_data_content(self): 
        serializer = CategorySerializer(instance = self.category)  
        data = serializer.data
        self.assertEqual(data['category_name'],'Test Product') 
        self.assertEqual(data['user'], self.user.id) 


class InventorySerializersTest(TestCase):   
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
            user= self.user,
            category= self.category,
            )
        self.inventory = Inventory.objects.create(
            transaction_type='inbound',
            unit_type='weight(kg)',
            quantity=200.0,
            date='2025-07-22T18:38:45.703898Z', 
            user= self.user,
            product=self.product   
        )
        
    def test_inventory_seializer_contains_expected_fields(self):
        serializer = InventorySerializer(instance = self.inventory) 
        data = serializer.data   
        self.assertEqual(set(data.keys()),{
            'id','transaction_type','unit_type','quantity','date','user','product'    
        })     
    
    
    def test_inventory_seializer_data_content(self): 
        serializer = InventorySerializer(instance = self.inventory)  
        data = serializer.data
        self.assertEqual(data['transaction_type'],'inbound') 
        self.assertEqual(data['unit_type'],'weight(kg)') 
        self.assertEqual(data['quantity'],200.0) 
        self.assertEqual(data['date'],'2025-07-22T18:38:45.703898Z')
        self.assertEqual(data['user'], self.user.id)   
        self.assertEqual(data['product'], self.product.id)       
        
        
class OrderSerializersTest(TestCase):     
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass') 
        self.order = Order.objects.create(
            order_number =1234,
            transaction_type ='Purchase',
            role = 'customer',
            role_name='Ali',
            date='2025-07-22T18:38:45.703898Z',
            status ='Completed',
                
        )           
    
    def test_order_seializer_contains_expected_fields(self):
        serializer = OrderSerializer(instance = self.order) 
        data = serializer.data   
        self.assertEqual(set(data.keys()),{
            'id','order_number','transaction_type','role','role_name','date','status'    
        })    
        
    def test_order_seializer_data_content(self): 
        serializer = OrderSerializer(instance = self.order)  
        data = serializer.data
        self.assertEqual(data['order_number'],1234) 
        self.assertEqual(data['transaction_type'],'Purchase') 
        self.assertEqual(data['role'],'customer') 
        self.assertEqual(data['role_name'],'Ali')
        self.assertEqual(data['date'], '2025-07-22T18:38:45.703898Z')   
        self.assertEqual(data['status'], 'Completed')   
        
        
class OrderLineSerializersTest(TestCase):   
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
            user= self.user,
            category= self.category,
            ) 
        self.order = Order.objects.create(
            order_number =1234,
            transaction_type ='Purchase',
            role = 'customer',
            role_name='Ali',
            date='2025-07-22T18:38:45.703898Z',
            status ='Completed',
                
        )
        
        self.orderline = OrderLine.objects.create(
            price =200.00,
            quantity=400,
            order =self.order,
            product =self.product    
        )        
    def test_orderline_seializer_contains_expected_fields(self):
        serializer = OrderLineSerializer(instance = self.orderline) 
        data = serializer.data   
        self.assertEqual(set(data.keys()),{
            'id','price','quantity','order','product'    
        })    
            
    def test_orderline_seializer_data_content(self): 
        serializer = OrderLineSerializer(instance = self.orderline)  
        data = serializer.data
        self.assertEqual(data['price'],'200.00') 
        self.assertEqual(data['quantity'],400) 
        self.assertEqual(data['order'],self.order.id) 
        self.assertEqual(data['product'],self.product.id)
           