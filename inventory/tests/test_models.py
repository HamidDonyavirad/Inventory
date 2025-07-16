from django.test import TestCase
from inventory.models import Product, Category,Inventory,Order,OrderItem
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hamid', password='123456789')
        self.category = Category.objects.create(category_name='Fruits', user=self.user)
        
    def test_create_product(self):
        product = Product.objects.create(
            product_name='banana',
            product_code=123,
            weight=5,
            color='yellow',
            dimensions='23*12*15',
            country_of_manufacture='usa',
            brand='usa',
            expiration_date=datetime.date(2025, 7, 12),
            category=self.category,
            user=self.user
        )
        
        self.assertEqual(product.product_name, 'banana')
        self.assertEqual(product.product_code, 123)
        self.assertEqual(product.weight, 5)
        self.assertEqual(product.color, 'yellow')
        self.assertEqual(product.dimensions, '23*12*15')
        self.assertEqual(product.country_of_manufacture, 'usa')
        self.assertEqual(product.brand, 'usa')
        self.assertEqual(product.expiration_date, datetime.date(2025, 7, 12))
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.user, self.user)



class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hamid', password='123456789') 
        
    def test_create_category(self):
        category = Category.objects.create(
            category_name = 'Fruits', 
            user=self.user       
        )
        self.assertEqual(category.category_name,'Fruits')    
        self.assertEqual(category.user, self.user)
        

class InventoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hamid', password='123456789')
        self.category = Category.objects.create(category_name='Fruits', user=self.user)
        self.product = Product.objects.create(
            product_name='banana',
            product_code=123,
            weight=5,
            color='yellow',
            dimensions='23*12*15',
            country_of_manufacture='usa',
            brand='usa',
            expiration_date=datetime.date(2025, 7, 12),
            category=self.category,
            user=self.user
        )
        
        
    def test_create_inventory(self):
        inventory = Inventory.objects.create(
            transaction_type = 'INBOUND',
            unit_type = 'WEIGHT', 
            quantity = '4.5',
            date = datetime.date(2025, 7, 12),
            user=self.user,
            product=self.product,   
        )                 
        
        self.assertEqual(inventory.transaction_type,'INBOUND')
        self.assertEqual(inventory.unit_type,'WEIGHT')
        self.assertEqual(inventory.quantity,'4.5')
        self.assertEqual(inventory.date,datetime.date(2025, 7, 12))
        self.assertEqual(inventory.user, self.user)
        self.assertEqual(inventory.product, self.product)
        
        

class OrderModelTest(TestCase):
    def test_create_order(self):
        order = Order.objects.create(
            order_number = '123',
            transaction_type = 'PURCHASE',
            role = 'CUSTOMER',
            role_name = 'Hamed',
            date = datetime.date(2025, 7, 12),
            status = 'STATUS_IN_PROGRESS'
        )
        self.assertEqual(order.order_number,'123')
        self.assertEqual(order.transaction_type,'PURCHASE')
        self.assertEqual(order.role,'CUSTOMER')
        self.assertEqual(order.role_name,'Hamed')
        self.assertEqual(order.date,datetime.date(2025, 7, 12))
        self.assertEqual(order.status,'STATUS_IN_PROGRESS')  
        
        
              
class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hamid', password='123456789')
        self.category = Category.objects.create(category_name='Fruits', user=self.user)
        self.order = Order.objects.create(
            order_number = '123',
            transaction_type = 'PURCHASE',
            role = 'CUSTOMER',
            role_name = 'Hamed',
            date = datetime.date(2025, 7, 12),
            status = 'STATUS_IN_PROGRESS'
        )
        self.product = Product.objects.create(
            product_name='banana',
            product_code=123,
            weight=5,
            color='yellow',
            dimensions='23*12*15',
            country_of_manufacture='usa',
            brand='usa',
            expiration_date=datetime.date(2025, 7, 12),
            category=self.category,
            user=self.user
        )
        
    def test_create_orderitem(self):
        orderitem = OrderItem.objects.create(
            price = 12.20,
            quantity = 50,
            order = self.order,
            product = self.product
        )    
                    
        self.assertEqual(orderitem.price,12.20)
        self.assertEqual(orderitem.quantity,50)
        self.assertEqual(orderitem.order,self.order)
        self.assertEqual(orderitem.product,self.product)