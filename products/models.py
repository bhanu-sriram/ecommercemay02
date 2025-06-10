from django.contrib.auth.models import User
from django.db import models

class AuditData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Create your models here.
class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True
                                 ,related_name='products')


class Category(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

class OrderDetails(AuditData):
    orderdetails = models.BigIntegerField()
    product_qty = models.PositiveIntegerField()
    product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, blank=True
                                ,related_name='orderdetails')