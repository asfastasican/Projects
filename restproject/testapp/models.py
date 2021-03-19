from django.db import models

# Create your models here.
class Artical(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
