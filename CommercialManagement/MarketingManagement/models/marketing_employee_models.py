from common.base_models import BaseEmployeeModel
from django.db import models


class MarktingEmployeeModel(BaseEmployeeModel):

    DepartmentSpecificJobs = [
        ("Marketing Manager", "Marketing Manager"),
        ("Digital Marketing Specialist", "Digital Marketing Specialist"),
        ("Content Creator", "Content Creator"),
        ("SEO Specialist", "SEO Specialist"),
        ("HR Specialist", "HR Specialist"),
    ]

    department = models.CharField(max_length=100, choices=DepartmentSpecificJobs)

    class Meta:
        verbose_name = "Markting Employee"
        verbose_name_plural = "Markting Employees"

    def __str__(self):
        return super().__str__() + "Markting Employee"

    @classmethod
    def get_all(cls):
        return cls.objects.all()
