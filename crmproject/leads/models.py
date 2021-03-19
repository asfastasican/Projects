from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

#inheriting the User Abstract class and its fields 
class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

class lead(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
