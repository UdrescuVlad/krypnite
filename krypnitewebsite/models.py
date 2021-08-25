from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=400,null=True)
    origin = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name