from django.db import models
from django.contrib.auth.models import User

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    # todo: rating, reviews, stock amount, image

    def __str__(self) -> str:
        return self.name
    
class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # TODO: what about visitors without an account?
    
    def __str__(self) -> str:
        return f"Shopping cart {self.id}"
    
class ShoppingCartItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Cart item {self.id}"
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.RESTRICT)
    orderedAt = models.DateField()
    shippedAt = models.DateField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Order {self.id}"
    
class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255) # street, number
    city = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Address {self.id},{self.city}, {self.postalCode}"