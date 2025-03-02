# from rest_framework import serializers
# from ..models.models import *


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         exclude = ["created_at"]


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         exclude = ["created_at", "updated_at"]


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"


# class OrderItemSerializer(serializers.ModelSerializer):

#     product = ProductSerializer()

#     class Meta:
#         model = OrderItem
#         fields = "__all__"


# class SalesOrderSerializer(serializers.ModelSerializer):

#     customer = CustomerSerializer()
#     items = OrderItemSerializer(many=True)

#     class Meta:
#         model = SalesOrder
#         exclude = ["created_at", "updated_at"]


# class SupplierSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Supplier
#         exclude = ["created_at"]


# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     supplier = SupplierSerializer()

#     class Meta:
#         model = PurchaseOrder
#         exclude = ["created_at", "updated_at"]
