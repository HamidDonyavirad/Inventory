from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Product (models.Model):
    product_name = models.CharField(max_length=200)
    product_code = models.IntegerField(unique=True)
    weight = models.FloatField(help_text="weight in kilograms")
    color = models.CharField(max_length=100,null=True,blank=True)
    dimensions = models.CharField(max_length=200,null=True,blank=True)
    country_of_manufacture = models.CharField(max_length=200)
    brand = models.CharField(max_length=100,null=True,blank=True)
    expiration_date = models.DateField()
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product_name}-{self.product_code}"
    
 
 
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
       
    def __str__(self):
        return f"{self.category_name}"



class Inventory (models.Model):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    INTERNAL_TRANSFER = 'internal transfer'
    
    TRANSACTION_TYPE_CHOICES = [
        (INBOUND,'inbound'),
        (OUTBOUND,'outbound'),
        (INTERNAL_TRANSFER,'internal transfer'),
    ]
    
    WEIGHT = 'weight(kg)'
    COUNT = 'count'   
    
    UNIT_TYPE_CHOICES = [
        (WEIGHT,'weight(KG)'),
        (COUNT,'count'),
    ] 
    transaction_type = models.CharField(max_length=20,choices=TRANSACTION_TYPE_CHOICES,default=INBOUND)
    unit_type =models.CharField(max_length=20, choices=UNIT_TYPE_CHOICES, default=WEIGHT)
    quantity = models.FloatField()
    date = models.DateTimeField()
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transaction_type}"

    

class Order (models.Model):
    order_number = models.IntegerField(unique=True)
    
    PURCHASE = 'Purchase'
    SALE = 'Sale'

    TRANSACTION_TYPE_CHOICES = [
        (PURCHASE, 'Purchase'),
        (SALE, 'Sale'),
    ]
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        default=PURCHASE,
    )

    CUSTOMER = 'customer'
    SUPPLIER = 'supplier'
    
    COSTOMER_OR_SUPPLIER_CHOICE = [
        (CUSTOMER,'customer'),
        (SUPPLIER,'supplier'),
    ]
    
    
    role = models.CharField(
        max_length=10,choices=COSTOMER_OR_SUPPLIER_CHOICE,default=CUSTOMER,    
    )
    role_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    
    STATUS_IN_PROGRESS = 'In Progress'
    STATUS_COMPLETED = 'Completed'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_IN_PROGRESS,
    )
    
    def __str__(self):
        return f"{self.transaction_type}-{self.costomer_or_supplier_choices}"
    
    

class OrderItem (models.Model):
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"Order #{self.order.order_number} - Product: {self.product.product_name}"
    
    
                