from django.contrib import admin
from .models import Group, UserProfile, Shift, Order, Product

admin.site.register(Group)
admin.site.register(UserProfile)
admin.site.register(Shift)
admin.site.register(Order)
admin.site.register(Product)
