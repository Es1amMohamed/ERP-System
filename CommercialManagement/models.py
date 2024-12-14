from django.db import models
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=245)
    phone = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    @classmethod
    def last_month(cls):
        
        las_month = now() - timedelta(days=30)
        return cls.objects.filter(created_at__gte=las_month).count()
    
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    year_of_production = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name
    
class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    class Meta:
        verbose_name = 'Sales Order'
        verbose_name_plural = 'Sales Orders'
        
    def __str__(self):
        return f"Sales Order #{self.id}"
    
    
class OrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        
    def __str__(self):
        return f"Order Item #{self.id}"
    
    
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('received', 'Received')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Orders'
        
    def __str__(self):
        return f"Purchase Order #{self.id}"
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()


    
    