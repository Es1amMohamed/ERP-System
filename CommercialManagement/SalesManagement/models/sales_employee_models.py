from src.common import base_models
from django.db import models


class SalesEmployeeModel(base_models.BaseEmployeeModel):
    JOB_TITLES = [
        ("HR_MANAGER", "HR Manager"),
        ("HR_SPECIALIST", "HR Specialist"),
        ("TEAM_LEADER", "Team Leader"),
        ("SALES_MANAGER", "Sales Manager"),
        ("SALES_REPRESENTATIVE", "Sales Representative"),
        ("MARKETING_MANAGER", "Marketing Manager"),
        ("MARKETING_SPECIALIST", "Marketing Specialist"),
        ("CUSTOMER_SERVICE_REP", "Customer Service Representative"),
        ("PROCUREMENT_MANAGER", "Procurement Manager"),
        ("FINANCIAL_ANALYST", "Financial Analyst"),
    ]

    job_title = models.CharField(max_length=50, choices=JOB_TITLES)

    def __str__(self):
        return f"name is {self.first_name} and email is {self.email}"

    @classmethod
    def count_by_job_title(cls, job_title):

        return cls.objects.filter(job_title=job_title).count()

    class Meta:
        verbose_name = "CM_Employee"
        verbose_name_plural = "CM_Employees"
