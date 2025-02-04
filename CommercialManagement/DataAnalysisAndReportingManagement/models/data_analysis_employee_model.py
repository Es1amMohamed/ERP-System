from common.base_models import BaseEmployeeModel
from django.db import models


class DataAnalysisEmployeeModel(BaseEmployeeModel):
    DepartmentSpecificJobs = [
        ("Data Analyst", "Data Analyst"),
        ("Business Intelligence Specialist", "Business Intelligence Specialist"),
        ("Reporting Specialist", "Reporting Specialist"),
        ("Database Administrator", "Database Administrator"),
        ("HR Specialist", "HR Specialist"),
    ]

    department = models.CharField(max_length=100, choices=DepartmentSpecificJobs)

    def __str__(self):
        return super().__str__() + "Data Analysis Employee"

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = "Data Analysis Employee"
        verbose_name_plural = "Data Analysis Employees"
