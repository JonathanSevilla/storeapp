from django.db import models
from django.conf import settings

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/' ,null=True, blank=True)

    def __str__(self):
        return self.name


class Stores(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Deals(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='logo/', null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ("user","store")

