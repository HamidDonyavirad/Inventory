from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from inventory.models import Product, Category,Inventory,Order,OrderItem
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
                
         
        