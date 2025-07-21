from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from inventory.models import Product, Category,Inventory,Order,OrderLine
import datetime
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class ProductViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(category_name='Test Product',user=self.user)
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        self.product_data = {
            'product_name': 'Test Product',
            'product_code': 12345,
            'weight': 1.5,
            'color': 'Red',
            'dimensions': '10x20x30',
            'brand': 'usa',
            'country_of_manufacture': 'usa',
            'expiration_date': '2025-07-12',
            'category': self.category.id,
            'user': self.user.id
        }
        
    def create_product(self, **kwargs):
        data = {
            'product_name': 'Test Product',
            'product_code': 12345,
            'weight': 1.5,
            'color': 'Red',
            'dimensions': '10x20x30',
            'brand': 'usa',
            'country_of_manufacture': 'usa',
            'expiration_date': datetime.date(2025, 7, 12),
            'category': self.category,
            'user': self.user
        }
        data.update(kwargs)
        return Product.objects.create(**data)
        
        
    def test_create_product_api(self):
        url = reverse('products')
        response = self.client.post(url,self.product_data,format='json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['product_name'],'Test Product')
        
    def test_get_product_api(self):
        product = self.create_product()
        url = reverse ('products') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >=1)  
        
    def test_update_product(self):
        product = self.create_product()
        url = reverse('product-detail', kwargs={'pk': product.id})      
        updated_data = self.product_data.copy()
        updated_data['product_name'] = 'Updated Name'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['product_name'], 'Updated Name')  
          
    def test_partial_update_product(self):
        product = self.create_product()
        url = reverse('product-detail', kwargs={'pk':product.id}) 
        patch_data ={'color': 'Blue'} 
        response = self.client.patch(url, patch_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['color'], 'Blue')  
        
    def test_delete_product(self):
        product = self.create_product()
        url = reverse('product-detail',kwargs={'pk':product.id})
        response =self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Product.objects.filter(id=product.id).exists())
                


class CategoryViewTest(APITestCase): 
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        
        self.category_data={
            'category_name':'test',
            'user': self.user.id
        } 
        
    def create_category(self,**kwargs):
        data={
            'category_name':'test1',
            'user': self.user      
            }
        data.update(kwargs)
        return Category.objects.create(**data)
        
        
        
    def test_create_category_api(self):
        url = reverse('category') 
        response = self.client.post(url,self.category_data,format = 'json')  
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['category_name'],'test') 
        
    def test_get_category_api(self):
        category = self.create_category()  
        url = reverse ('category') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >=1)  
                
    def test_update_category(self):
        category = self.create_category()
        url = reverse('category-detail', kwargs={'pk': category.id})      
        updated_data = self.category_data.copy()
        updated_data['category_name'] = 'Updated Name'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['category_name'], 'Updated Name')  
        
    def test_delete_category(self):
        categoty = self.create_category()
        url = reverse('category-detail',kwargs={'pk':categoty.id})
        response =self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(id=categoty.id).exists())      
        
        

class InventoryViewTest(APITestCase): 
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass') 
        self.category = Category.objects.create(category_name='Test Product',user=self.user)
        
        
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token) 
        
        self.product = Product.objects.create(
            product_name= 'Test Product',
            product_code= 12345,
            weight= 1.5,
            color= 'Red',
            dimensions= '10x20x30',
            brand= 'usa',
            country_of_manufacture= 'usa',
            expiration_date= datetime.date(2025, 7, 12),
            category= self.category,
            user= self.user
        )
        
        self.inventory_data={
            'transaction_type':'inbound',
            'unit_type':'weight(kg)',
            'quantity':'200',
            'date':datetime.date(2025, 7, 12),
            'user': self.user.id,
            'product':self.product.id
        } 
        
    def create_inventory(self, **kwargs):
        data = {
            'transaction_type':'inbound',
            'unit_type':'weight(kg)',
            'quantity':'200',
            'date':datetime.date(2025, 7, 12),
            'user': self.user,
            'product':self.product
        }
        data.update(kwargs)
        return Inventory.objects.create(**data)
    
    def test_create_inventory_api(self):
        url = reverse('inventory') 
        response = self.client.post(url,self.inventory_data,format = 'json')  
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['transaction_type'],'inbound')             
        
    def test_get_inventory_api(self):
        Inventory = self.create_inventory()  
        url = reverse ('inventory') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >=1)    
        
    def test_delete_inventory(self):
        inventory = self.create_inventory()
        url = reverse('inventory-detail',kwargs={'pk':inventory.id})
        response =self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Inventory.objects.filter(id=inventory.id).exists())  
        

class OrderViewTest(APITestCase): 
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  
        
        self.order_data={
            'order_number':1234,
            'transaction_type':'Purchase',
            'role':'customer',
            'date':datetime.date(2025, 7, 12),
            'status':'In Progress'
            
        } 
        
    def create_order(self, **kwargs):
        data = {
            'order_number':1234,
            'transaction_type':'Purchase',
            'role':'customer',
            'date':datetime.date(2025, 7, 12),
            'status':'In Progress'
        }
        data.update(kwargs)
        return Order.objects.create(**data)
    
    def test_create_order_api(self):
        url = reverse('order') 
        response = self.client.post(url,self.order_data,format = 'json')  
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['order_number'],1234)    
    
    def test_get_order_api(self):
        order = self.create_order()  
        url = reverse ('order') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >=1)               
        
    def test_delete_order(self):
        order = self.create_order()
        url = reverse('order-detail',kwargs={'pk':order.id})
        response =self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Order.objects.filter(id=order.id).exists())    