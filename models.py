"""
Possible models structure for the given widget table.
"""
from django.db import models


class StockItem(models.Model):
    widget = models.ForeignKey('Widget', on_delete=models.PROTECT)
    packaging = models.ForeignKey('Package', on_delete=models.PROTECT)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT)
    cost = models.DecimalField(decimal_places=2, max_digits=8)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    min_qty = models.PositiveIntegerField(default=0)
    # ...


class Widget(models.Model):
    name = models.CharField(max_length=50)
    # ...


class Package(models.Model):
    name = models.CharField(max_length=20)
    item_count = models.PositiveSmallIntegerField(default=1)
    # ...


class Customer(models.Model):
    name = models.CharField(max_length=100)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_customers', on_delete=models.PROTECT)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_customers', on_delete=models.PROTECT)
    # ...


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    # ...


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(
        'Address', related_name='warehouses', on_delete=models.PROTECT)
    # ...


class Address(models.Model):
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    # ...
