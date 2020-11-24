from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.user)

class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/image/',null=True, blank=True)
    status = models.BooleanField()


    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    transaction = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        return total 

    @property
    def get_total_items(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total


class Orderitem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total