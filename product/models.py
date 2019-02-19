from django.db import models
from category.models import Category
from brand.models import Brand

# Create your models here.
class Product(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productName = models.CharField(max_length=120)
    productPrice = models.TextField()

    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
