from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address"]
    list_filter = [
        "name",
    ]
    search_fields = ["name", "email", "phone", "address"]
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity", "category"]
    list_filter = [
        "category",
    ]
    search_fields = ["name", "category__name"]
    list_per_page = 10

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = [
        "name",
    ]
    search_fields = [
        "name",
    ]
    list_per_page = 10


class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "total_amount"]
    list_filter = ["customer", "product"]
    search_fields = ["customer__name", "product__name"]
    list_per_page = 10


class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address"]
    list_filter = [
        "name",
    ]
    search_fields = ["name", "email", "phone", "address"]
    list_per_page = 10


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["supplier", "total_amount"]
    list_filter = ["supplier"]
    search_fields = ["supplier__name"]
    list_per_page = 10


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
