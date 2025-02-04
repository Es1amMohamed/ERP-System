from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from CommercialManagement.SalesManagement.models import Product


class PriceManagement(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices"
    )
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Base Price"
    )
    effective_date = models.DateField(
        verbose_name="Effective Date",
        help_text="Date when this price becomes effective",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Price Management"
        verbose_name_plural = "Price Managements"

    def __str__(self):
        return f"{self.product.name} - {self.base_price} (Effective: {self.effective_date})"

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


class Discount(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="discounts"
    )
    discount_type = models.CharField(
        max_length=10,
        choices=[("fixed", "Fixed Amount"), ("percentage", "Percentage")],
        default="percentage",
    )
    value = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Discount Value",
    )
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def get_discounted_price(self, base_price):
        if self.discount_type == "percentage":
            return base_price * (1 - self.value / 100)
        return max(base_price - self.value, 0)

    def __str__(self):
        return f"{self.product.name} - {self.value} {self.get_discount_type_display()} Discount"


class Promotion(models.Model):
    name = models.CharField(max_length=255, verbose_name="Promotion Name")
    description = models.TextField(blank=True, null=True)
    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, related_name="promotions"
    )
    min_quantity = models.PositiveIntegerField(
        default=1, verbose_name="Minimum Quantity Required"
    )
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.name


class PricingRule(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="pricing_rules"
    )
    min_quantity = models.PositiveIntegerField(verbose_name="Minimum Quantity")
    max_quantity = models.PositiveIntegerField(
        verbose_name="Maximum Quantity", null=True, blank=True
    )
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Discounted Price"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pricing Rule"
        verbose_name_plural = "Pricing Rules"

    def __str__(self):
        return f"{self.product.name} - {self.min_quantity} to {self.max_quantity} - {self.discounted_price}"
