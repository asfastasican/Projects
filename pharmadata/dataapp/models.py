from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    pid=models.IntegerField()
    description=models.TextField()
    contents=models.CharField(max_length=256)
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Doctor(models.Model):
    DoctorName=models.CharField(max_length=256)
    DLicense=models.CharField(max_length=256)
    HospitalName=models.CharField(max_length=256)
    Address=models.TextField()
    City=models.CharField(max_length=256)
    State=models.CharField(max_length=256)
    PinCode=models.IntegerField()
    Contactno=models.IntegerField()
    Email=models.EmailField()

    def __str__(self):
        return self.DoctorName


class Medical(models.Model):
    MownerName=models.CharField(max_length=256)
    MLicense=models.CharField(max_length=256)
    MedicalName=models.CharField(max_length=256)
    Address=models.TextField()
    City=models.CharField(max_length=256)
    State=models.CharField(max_length=256)
    PinCode=models.IntegerField()
    Contactno=models.IntegerField()
    Email=models.EmailField()

    def __str__(self):
        return self.MownerName


class Organization(models.Model):
    OwnerName=models.CharField(max_length=256)
    OLicense=models.CharField(max_length=256)
    OrgName=models.CharField(max_length=256)
    Address=models.TextField()
    City=models.CharField(max_length=256)
    State=models.CharField(max_length=256)
    PinCode=models.IntegerField()
    Contactno=models.IntegerField()
    Email=models.EmailField()

    def __str__(self):
        return self.OwnerName

class Stocks(models.Model):
    product=models.OneToOneField(Product,on_delete=models.SET_NULL,blank=True,null=True)
    Maximum_quantity=models.IntegerField(default=1000)
    current_quantity=models.IntegerField()

class Sale(models.Model):
    product=models.OneToOneField(Product,on_delete=models.SET_NULL,blank=True,null=True)
    quater1_sale=models.IntegerField(blank=True,null=True)
    quater2_sale=models.IntegerField(blank=True,null=True)
    quater3_sale=models.IntegerField(blank=True,null=True)
    quater4_sale=models.IntegerField(blank=True,null=True)
