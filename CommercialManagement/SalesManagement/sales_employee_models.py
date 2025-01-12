from common.basemodels import BaseEmployeeModel
from django.db import models


class SalesEmployeeModel(BaseEmployeeModel):
    DepartmentSpecificJobs = [
        ("Sales Manager", "Sales Manager"),
        ("Sales Representative", "Sales Representative"),
        ("Sales Team Leader", "Sales Team Leader"),
        ("Sales Analyst", "Sales Analyst"),
        ("Sales Associate", "Sales Associate"),
        ("HR Specialist", "HR Specialist"),
    ]

    department = models.CharField(max_length=100, choices=DepartmentSpecificJobs)

    def __str__(self):
        return super().__str__() + "Sales Employee"

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = "Sales Employee"
        verbose_name_plural = "Sales Employees"
