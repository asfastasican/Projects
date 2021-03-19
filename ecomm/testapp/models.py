from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(blank=False)
    product_description=models.TextField(max_length=400,blank=True,null=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    #method to avoid image attribute Error in the absence of image
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url



class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False,blank=False)
    transaction_id=models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total  for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=1,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def add_quantity(self):
        added_quantity=self.quantity= self.quantity + 1
        return added_quantity


    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
