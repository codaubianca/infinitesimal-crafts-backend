from django.contrib import admin
from . import models

admin.site.register(models.Supplier)
admin.site.register(models.Product)
admin.site.register(models.ShoppingCart)
admin.site.register(models.ShoppingCartItem)
admin.site.register(models.Order)
admin.site.register(models.ShippingAddress)