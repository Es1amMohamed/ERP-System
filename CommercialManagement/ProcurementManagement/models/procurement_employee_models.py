from src.common.base_models import BaseEmployeeModel
from django.db import models


class ProcurementEmployeeModel(BaseEmployeeModel):

    DepartmentSpecificJobs = [
        ("Procurement Manager", "Procurement Manager"),
        ("Procurement Officer", "Procurement Officer"),
        ("Vendor Relations Manager", "Vendor Relations Manager"),
        ("Inventory Coordinator", "Inventory Coordinator"),
        ("HR Specialist", "HR Specialist"),
    ]

    department = models.CharField(max_length=100, choices=DepartmentSpecificJobs)

    def __str__(self):
        return super().__str__() + " Procurement Employee "

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = "Procurement Employee"
        verbose_name_plural = "Procurement Employees"
