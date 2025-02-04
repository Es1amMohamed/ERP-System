from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .marketing_employee_models import MarktingEmployeeModel


class CampaignModel(models.Model):
    marketer = models.ForeignKey(
        MarktingEmployeeModel, on_delete=models.PROTECT, verbose_name=("Marketer")
    )
    name = models.CharField(max_length=200, verbose_name=("Campaign Name"))
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=("Budget")
    )
    description = models.TextField()
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Discount (%)",
        help_text="Enter discount percentage (0-100)",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return self.name


class CampaignTargetModel(models.Model):
    campaign = models.ForeignKey(CampaignModel, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Campaign Target"
        verbose_name_plural = "Campaign Targets"

    def __str__(self):
        return self.name
