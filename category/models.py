from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoryname = models.CharField(max_length=120)

    def __str__(self):
        return self.categoryname

    description = models.TextField()