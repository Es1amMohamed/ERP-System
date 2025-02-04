from django.db import models
from .procurement_employee_models import ProcurementEmployeeModel


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()


class PurchaseOrder(models.Model):
    procurement_employee = models.ForeignKey(
        ProcurementEmployeeModel, on_delete=models.PROTECT
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=[("pending", "Pending"), ("received", "Received")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

    def __str__(self):
        return f"Purchase Order #{self.id}"

    @classmethod
    def get_all(cls):
        return cls.objects.all()


class PurchaseItem(models.Model):
    PurchaseStatus = (
        ("pending", "Pending"),
        ("received", "Received"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    )

    name = models.CharField(max_length=255, verbose_name=("Item Name"))
    description = models.TextField(blank=True, null=True, verbose_name=("Description"))
    quantity = models.PositiveIntegerField(verbose_name=("Quantity"))
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=("Unit Price")
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="purchase_items",
        verbose_name=("Supplier"),
    )
    order_date = models.DateField(auto_now_add=True, verbose_name=("Order Date"))
    delivery_date = models.DateField(
        null=True, blank=True, verbose_name=("Expected Delivery Date")
    )
    status = models.CharField(
        max_length=10,
        choices=PurchaseStatus,
        default="pending",
        verbose_name=("Status"),
    )

    def total_cost(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name} - {self.supplier.name}"
