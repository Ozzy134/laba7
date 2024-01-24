from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    group = models.CharField(max_length=20)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Shift(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    employee = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Order(models.Model):
    table_number = models.IntegerField()
    employee = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    positions = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.IntegerField()

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)


