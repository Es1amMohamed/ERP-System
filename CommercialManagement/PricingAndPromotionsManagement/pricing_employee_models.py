from common.basemodels import BaseEmployeeModel
from django.db import models


class PricingEmployeeModel(BaseEmployeeModel):

    DepartmentSpecificJobs = [
        ("Pricing Manager", "Pricing Manager"),
        ("Promotions Manager", "Promotions Manager"),
        ("Campaign Coordinator", "Campaign Coordinator"),
        ("Market Research Analyst", "Market Research Analyst"),
        ("HR Specialist", "HR Specialist"),
    ]

    department = models.CharField(max_length=100, choices=DepartmentSpecificJobs)

    def __str__(self):
        return super().__str__() + "Pricing And Promotions Employee"

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = "Pricing Employee"
        verbose_name_plural = "Pricing Employees"
